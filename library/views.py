from rest_framework.viewsets import ModelViewSet

from library.models import Reader, Author, Books
from library.serializers import BooksSerializer, ReaderSerializer, AuthorSerializer


""" CRUD для моделей """


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
