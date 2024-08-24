from django.contrib import admin
from .models import BooksModel


# Register your models here.

class AdminBook(admin.ModelAdmin):
    list_display = ['rdate', 'bookname', 'author', 'rating']


admin.site.register(BooksModel, AdminBook)
