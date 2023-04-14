# Create your views here.
from rest_framework.decorators import api_view
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from rest_framework.permissions import IsAuthenticated
from book.models import Book, Author, BookInstance
from .pagination import DefaultPageNumberPagination
from .permissions import IsAdminOrReadOnly
from .serializers import BookSerializer, BookCreatedSerializer, AuthorSerializer, BookInstanceSerializer
from rest_framework import generics, status

"""
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        book = BookCreatedSerializer(data=request.data)
        book.is_valid(raise_exception=True)
        book.save()
        return Response("book saved successfully")


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_details(request, id):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def author_details(request, first_name, last_name):
    if request.method == 'GET':
        author = get_object_or_404(Author, first_name, last_name)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

"""


class AuthorViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookInstanceViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer


class BookViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# change this class to bookAuthorView
class BookCreateApiView(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    message = 'smile is sleeping because her code is not running'
    subject = 'smile must do django'
    send_mail(subject, message, '', ['orelovly@gmail.com'])
    # send_mass_mail
    return Response(serializer.data)


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all
    serializer_class = AuthorSerializer


class BookInstanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookInstance.objects.all
    serializer_class = BookInstanceSerializer


class GetAuthorById(generics.ListAPIView):
    def get(self, request, id):
        try:
            author = Author.object.get(pk=id)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetAllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
