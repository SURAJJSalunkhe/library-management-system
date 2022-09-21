from django.db import models
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    barcode = models.CharField(max_length=30)


    class Meta:
        db_table = "BOOK_INFORMATION"


