from django.db import models


class Issue(models.Model):
    app_label = "issues"

    junior_id = models.PositiveIntegerField(blank=True, null=True)
    senior_id = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
