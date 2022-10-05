
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Book
from .serializers import BookSerializer, UserSerializer
from django.contrib.auth.models import User


class BookViewset(viewsets.ModelViewSet):
    """
        This API is used to get, post, update and delete book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class StudentBookViewset(viewsets.ModelViewSet):
    """
        This API is used to get all books for student without login
    """
    http_method_names = ['get']
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny, )


class UserViewset(viewsets.ModelViewSet):
    """
        This API is used to get and create user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

