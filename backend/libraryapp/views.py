from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from libraryapp.models import Author, Book
from libraryapp.serializers import AuthorSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['POST'])
def save_author(request):
    author = Author()
    author.firstName = request.data['firstName']
    author.lastName = request.data['lastName']
    author.dateOfBirth = request.data['dateOfBirth']

    Author.save(author)
    return Response(status=status.HTTP_201_CREATED)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
