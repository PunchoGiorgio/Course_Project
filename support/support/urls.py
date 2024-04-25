import datetime
import json
import random
import string
from typing import Callable

import requests
from django.http import HttpRequest, JsonResponse
from django.urls import path

variable = 777

date = datetime.datetime.now()
obj = date.strftime("%H:%M:%S")


def f(size):
    return "".join([random.choice(string.ascii_letters) for _ in range(size)])


create_random_string: Callable[[int], str] = f


def generate_article_idea(request: HttpRequest) -> JsonResponse:
    content = {
        "title": create_random_string(size=10),
        "description": create_random_string(size=20),
    }
    return JsonResponse(content)


def get_current_market_state(request: HttpRequest) -> JsonResponse:

    API_URL = "https://alphavantage.co/query"

    data = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "USD",
        "to_currency": "UAH",
        "apikey": "UHDZLAS4WZSOC9BW",
    }

    response = requests.post(API_URL, params=data)

    new_data = ({"timestamp": obj},)

    with open("status.json") as f:
        status_data = json.load(f)

        status_data["results"] += list(new_data)

    with open("status.json", "w") as p:
        json.dump(status_data, p)

    with open("status.json") as k:
        update_data = json.load(k)

        if len(update_data["results"]) <= 1:
            rate = response.json()["Realtime Currency Exchange Rate"][
                "5. Exchange Rate"
            ]
            return JsonResponse({"rate": rate})

        else:
            date_time_obj1 = datetime.datetime.strptime(
                update_data["results"][-2]["timestamp"], "%H:%M:%S"
            )
            date_time_obj2 = datetime.datetime.strptime(
                update_data["results"][-1]["timestamp"], "%H:%M:%S"
            )

            time_delta = date_time_obj2 - date_time_obj1
            seconds = time_delta.total_seconds()

            if seconds < 30:
                rate = variable
                return JsonResponse({"rate": rate})
            else:
                rate = response.json()["Realtime Currency Exchange Rate"][
                    "5. Exchange Rate"
                ]
                return JsonResponse({"rate": rate})


urlpatterns = [
    path(route="generate-article", view=generate_article_idea),
    path(route="market", view=get_current_market_state),
]
