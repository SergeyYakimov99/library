from django.db import models

#NULLABLE = {'blank': True, 'null': True}


class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    name = models.CharField(verbose_name="Имя", max_length=20)
    surname = models.CharField(verbose_name="Фамилия", max_length=20)
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
    description = models.TextField(verbose_name="Описание", max_length=2000)
    count_page = models.IntegerField(verbose_name="Всего страниц")
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE, null=True)
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
    surname = models.CharField(verbose_name="Фамилия", max_length=20)
    telephone = models.BigIntegerField(verbose_name="Телефон", unique=True)
    status = models.BooleanField(verbose_name="Статус", default=True)
    active_books = models.ManyToManyField(Books, verbose_name="Активные книги")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    def __str__(self):
        return f"{self.name} {self.surname}"

    def display_active_books(self):
        return ', '.join([books.title for books in self.active_books.all()])

    display_active_books.short_description = 'Активные книги'
