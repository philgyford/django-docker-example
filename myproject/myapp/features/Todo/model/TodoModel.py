from django.db import models


class TodoTask(models.Model):
    todo_id = models.BigAutoField(primary_key=True)
    todo_title = models.CharField(max_length=200)
    todo_start_date = models.DateTimeField("Task Start Date")
    todo_end_date = models.DateTimeField("Task End Date")
    todo_status_is_finished = models.BooleanField("Is Finished")
    todo_status_is_archived = models.BooleanField("Is Archived")
    todo_status_success_rate = models.FloatField("Success Rate")
