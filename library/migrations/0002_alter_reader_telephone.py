# Generated by Django 4.1.6 on 2023-03-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='telephone',
            field=models.BigIntegerField(null=True, verbose_name='Телефон'),
        ),
    ]