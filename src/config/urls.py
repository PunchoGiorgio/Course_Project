from django.contrib import admin
from django.urls import path

from issues.api import get_issues

urlpatterns = [
    path("admin/", admin.site.urls),
    path("issues/", get_issues),
]
