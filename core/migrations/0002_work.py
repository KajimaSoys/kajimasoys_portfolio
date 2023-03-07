# Generated by Django 4.1.5 on 2023-02-24 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('name', models.CharField(max_length=250, verbose_name='Название работы')),
                ('description', models.TextField(blank=True, max_length=5000, verbose_name='Описание')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка на компанию, где работа')),
                ('isActive', models.BooleanField(default=True, verbose_name='Активен?')),
            ],
            options={
                'verbose_name': 'Работа',
                'verbose_name_plural': 'Работы',
            },
        ),
    ]