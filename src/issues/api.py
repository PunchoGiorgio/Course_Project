from django.http import HttpRequest, JsonResponse

from issues.models import Issue


def get_issues(request: HttpRequest) -> JsonResponse:

    jun = 10

    sen = 27

    question = "What is Python?"

    answer = "Python is a widely-used general-purpose, high-level programming language."

    Issue.objects.create(junior_id=jun, senior_id=sen, title=question, body=answer)

    result = Issue.objects.filter(junior_id=3).values()

    return JsonResponse({"data": list(result)})
