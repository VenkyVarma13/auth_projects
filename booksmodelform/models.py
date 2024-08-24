from django.db import models


# Create your models here.
class BooksModel(models.Model):
    rdate = models.CharField(max_length=20)
    bookname = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    rating = models.IntegerField()
