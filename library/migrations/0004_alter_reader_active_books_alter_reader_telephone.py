# Generated by Django 4.1.6 on 2023-03-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_books_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='active_books',
            field=models.ManyToManyField(blank=True, null=True, to='library.books', verbose_name='Активные книги'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='telephone',
            field=models.BigIntegerField(verbose_name='Телефон'),
        ),
    ]