from django.db import models


class DiaryModel(models.Model):
    diary_id = models.BigAutoField(primary_key=True)
    diary_description = models.CharField(max_length=6000)
    diary_date = models.DateTimeField("event Date", auto_now_add=True)
    diary_success_rate = models.FloatField("Success Rate")
