
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet

from library.models import Reader, Author, Books
from library.permissions import PermissionPolicyMixin, OnlyReader
from library.serializers import BooksSerializer, ReaderSerializer, AuthorSerializer


""" CRUD для моделей """


class BooksViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes_per_method = {
        'create': [IsAdminUser],
        'retrieve': [AllowAny],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }


class ReaderViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes_per_method = {
        'create': [AllowAny],
        'retrieve': [IsAdminUser | OnlyReader],
        'update': [IsAdminUser | OnlyReader],
        'destroy': [IsAdminUser | OnlyReader],
    }


class AuthorViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes_per_method = {
        'create': [IsAdminUser],
        'retrieve': [AllowAny],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }
