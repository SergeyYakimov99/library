from rest_framework import serializers

from library.models import Reader, Books, Author


class Count_pageValidator:

    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError('количество страниц не может быть меньше 0')


class PhoneValidator:

    def __call__(self, value):
        rez = Reader.objects.all().filter(telephone=value)
        if rez:
            raise serializers.ValidationError('данный телефон уже используется, введите другой номер')
        value = str(value)
        if len(value) != 11:
            raise serializers.ValidationError('номер должен состоять из 11 цифр')
        if value[0] != '7':
            raise serializers.ValidationError('номер должен начинаться на 7')


class ReaderSerializer(serializers.ModelSerializer):
    telephone = serializers.IntegerField(validators=[PhoneValidator()])
    active_books = serializers.SlugRelatedField(queryset=Books.objects.all(), slug_field='title', many=True)

    def validate(self, attrs):
        if len(attrs['active_books']) > 3:
            raise serializers.ValidationError('Невозможно добавить более 3 книг')
        return attrs

    def create(self, validated_data):
        reader = super().create(validated_data)
        reader.set_password(reader.password)
        reader.save()

        return reader

        # for book in validated_data['active_books']:
        #     if book.count_books == 0:
        #         raise serializers.ValidationError(f'Невозможно добавить книгу "{book.title}", нет в наличии!')
        # return super().create(validated_data)

    def update(self, instance, validated_data):
        for book in validated_data['active_books']:
            if book.count_books == 0:
                raise serializers.ValidationError(f'Невозможно добавить книгу "{book.title}", нет в наличии!')
        return super().update(instance, validated_data)

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
