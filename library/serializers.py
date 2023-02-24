from rest_framework import serializers

from library.models import Reader, Books, Author


class ReaderSerializer(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(queryset=Books.objects.all(), slug_field='title', many=True)

    class Meta:
        model = Reader
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='surname', many=True)

    class Meta:
        model = Books
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
