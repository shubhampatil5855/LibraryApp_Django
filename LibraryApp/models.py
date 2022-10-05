from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    isbn = models.IntegerField()
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()


