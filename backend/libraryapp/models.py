from django.db import models


# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.DateField()


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)