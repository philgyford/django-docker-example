from django.contrib import admin
from myproject.myapp.features.Todo.model.TodoModel import TodoTask
from myproject.myapp.features.Diary.model.DiaryModel import DiaryModel
from myproject.myapp.features.LifeEvents.model.LifeEventModel import LifeEvent
from myproject.myapp.features.Books.model.BookModel import BookModel

# Register your models here.

admin.site.register(TodoTask)
admin.site.register(DiaryModel)
admin.site.register(BookModel)
admin.site.register(LifeEvent)
