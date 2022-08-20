from django.contrib import admin
from todoApp.models import ToDoItem, ToDoList


# Register your models here.

admin.site.register(ToDoItem)
admin.site.register(ToDoList)