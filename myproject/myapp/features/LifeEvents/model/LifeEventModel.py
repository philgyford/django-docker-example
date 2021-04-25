from django.db import models


class LifeEvent(models.Model):
    life_event_id = models.BigAutoField(primary_key=True)
    life_event_title = models.CharField(max_length=600)
    life_event_date = models.DateTimeField("event Date")
    life_event_success_rate = models.FloatField("Success Rate")
