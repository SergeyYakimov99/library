from rest_framework import serializers

from library.models import Reader, Books, Author


class PhoneValidator:
    # def __init__(self):
    #     pass

    def __call__(self, value):
        value = str(value)
        if len(value) != 11:
            raise serializers.ValidationError('номер должен состоять из 11 цифр')
        if value[0] != '7':
            raise serializers.ValidationError('номер должен начинаться на 7')

class ReaderSerializer(serializers.ModelSerializer):
    telephone = serializers.IntegerField(validators=[PhoneValidator()])
    active_books = serializers.SlugRelatedField(queryset=Books.objects.all(), slug_field='title', many=True)

    class Meta:
        model = Reader
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='surname', many=True,
                                          default='Неизвестный')

    class Meta:
        model = Books
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
