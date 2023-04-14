from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class LibraryUser(AbstractUser):
    email = models.EmailField(unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    date_of_death = models.DateField(blank=True, null=True, default='0000-00-00')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    GENRE_CHOICES = [

        ('FINANCE', 'FIN'),
        ('POLITICS', 'POL'),
        ('POWER', 'POW'),
        ('COMEDY', 'COM')
    ]

    LANGUAGE_CHOICES = [
        ('ENGLISH', 'ENG'),
        ('HAUSA', 'HAU'),
        ('IGBO', 'IGB'),
        ('YORUBA', 'YOR')


    ]

    title = models.CharField(max_length=255, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    genre = models.CharField(max_length=200, blank=False, null=False)
    language = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='books')
    imprint = models.CharField(max_length=255, null=False, blank=False)
    borrower = models.OneToOneField(LibraryUser, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.imprint
