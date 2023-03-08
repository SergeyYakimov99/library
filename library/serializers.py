from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from library.models import Reader, Books, Author


class Count_pageValidator:

    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError('количество страниц не может быть меньше 0')


class PhoneValidator:

    def __call__(self, value):
        value = str(value)
        if len(value) != 11:
            raise serializers.ValidationError('номер должен состоять из 11 цифр')
        if value[0] != '7':
            raise serializers.ValidationError('номер должен начинаться на 7')


class BooksValidator:

    def validate(self, attrs):
        if len(attrs['active_books']) > 3:
            raise serializers.ValidationError('Невозможно добавить более 3 книг')
        return attrs


class ReaderSerializer(serializers.ModelSerializer):
    telephone = serializers.IntegerField(validators=[PhoneValidator()])
    active_books = serializers.SlugRelatedField(queryset=Books.objects.all(), slug_field='title', many=True,
                                                validators=[BooksValidator()])

    class Meta:
        model = Reader
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='surname')
    count_page = serializers.IntegerField(validators=[Count_pageValidator()])

    class Meta:
        model = Books
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
