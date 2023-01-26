# Generated by Django 4.1.5 on 2023-01-23 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('name', models.CharField(max_length=100, verbose_name='Название группы')),
            ],
            options={
                'verbose_name': 'Группа работ',
                'verbose_name_plural': 'Группы работ',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('name', models.CharField(max_length=250, verbose_name='Название работы')),
                ('description', models.TextField(blank=True, max_length=5000, verbose_name='Описание')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка на компанию, где работа')),
            ],
            options={
                'verbose_name': 'Работа',
                'verbose_name_plural': 'Работы',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('name', models.CharField(max_length=250, verbose_name='Название группы')),
                ('description', models.TextField(blank=True, max_length=5000, verbose_name='Описание')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка на проект')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]