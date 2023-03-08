from rest_framework.exceptions import ValidationError
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

    def update(self, instance, validated_data):
        if validated_data['active_books']:
        # Уменьшаем количество экземпляров книги, если книга добавляется в актив читателя
            for book in validated_data['active_books']:
                if book not in instance.active_books.all():
                    if book.quantity > 0:
                        book.quantity -= 1
                        book.save()
                    else:
                        raise ValidationError(f'Книга "{book.title}" отсутствует')
        # Увеличиваем количество экземпляров книги, если книга удаляется из актива читателя
            for book in instance.active_books.all():
                if book not in validated_data['active_books']:
                    book.quantity += 1
                    book.save()
        return super().update(instance, validated_data)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
