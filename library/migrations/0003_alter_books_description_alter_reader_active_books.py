# Generated by Django 4.1.6 on 2023-02-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_author_created_alter_author_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='active_books',
            field=models.ManyToManyField(blank=True, to='library.books', verbose_name='Активные книги'),
        ),
    ]
