# Generated by Django 4.1.5 on 2023-01-07 01:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_citiesdiagram_image_raw_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citiesdiagram',
            name='image_raw',
            field=models.ImageField(upload_to='cache/', verbose_name='Картинка в чистом виде'),
        ),
        migrations.AlterField(
            model_name='citiesvacanciesdiagram',
            name='image_raw',
            field=models.ImageField(upload_to='cache/', verbose_name='Картинка в чистом виде'),
        ),
        migrations.AlterField(
            model_name='professiondescriptionblock',
            name='description',
            field=ckeditor.fields.RichTextField(default='Без описания', verbose_name='Текст описания'),
        ),
        migrations.AlterField(
            model_name='vacanciesdiagram',
            name='image_raw',
            field=models.ImageField(upload_to='cache/', verbose_name='Картинка в чистом виде'),
        ),
        migrations.AlterField(
            model_name='yeardiagram',
            name='image_raw',
            field=models.ImageField(upload_to='cache/', verbose_name='Картинка в чистом виде'),
        ),
    ]