from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.templatetags.i18n import language

from .models import Book, Author, BookInstance, LibraryUser


# Register your models here.
# @admin.register(LibraryUser)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'genre', 'language', 'price']
    list_editable = ['price']
    list_per_page = 10
    list_filter = ['title']


@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'date_of_birth']


@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_display = ['unique_id', 'due_back', 'imprint', 'borrower']
