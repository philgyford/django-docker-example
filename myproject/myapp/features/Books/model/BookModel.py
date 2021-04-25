from django.db import models


class BookModel(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    book_title = models.CharField(max_length=6000)
    book_start_date = models.DateTimeField("book start reading Date", auto_now_add=True)
    book_end_date = models.DateTimeField("book end reading Date", auto_now_add=True)
    current_page = models.IntegerField("current page")
    page_count = models.IntegerField("current page")

