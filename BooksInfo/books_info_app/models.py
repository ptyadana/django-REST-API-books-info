from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=300)
    author_name = models.CharField(max_length=300)
    book_price = models.IntegerField()
    book_quantity = models.IntegerField()

    def __str__(self):
        return self.book_name