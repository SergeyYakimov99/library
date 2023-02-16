from django.db import models


class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    name = models.CharField(verbose_name="Имя", max_length=20)
    surname = models.CharField(verbose_name="Фамилия", max_length=20, unique=True)
    image = models.ImageField(verbose_name="Фото", upload_to='pictures/')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    def __str__(self):
        return f"{self.name} {self.surname}"


class Books(models.Model):
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    title = models.CharField(verbose_name="Название", max_length=200)
    description = models.CharField(verbose_name="Описание", max_length=1000)
    count_page = models.IntegerField(verbose_name="Страниц")
    author = models.ManyToManyField(Author, verbose_name="Автор")
    count_books = models.IntegerField(verbose_name="Количество книг")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    def __str__(self):
        return self.title


class Reader(models.Model):
    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"
        # ordering = "created"

    name = models.CharField(verbose_name="Имя", max_length=20)
    surname = models.CharField(verbose_name="Фамилия", max_length=20, unique=True)
    telephone = models.BigIntegerField(verbose_name="Телефон")
    status = models.BooleanField(verbose_name="Статус", default=True)
    active_books = models.ManyToManyField(Books, verbose_name="Активные книги")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    def __str__(self):
        return f"{self.name} {self.surname}"
