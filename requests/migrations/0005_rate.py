# Generated by Django 4.1.5 on 2023-03-14 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_alter_order_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('about', 'About page'), ('cookie', 'Cookie page'), ('main', 'Main page'), ('privacy', 'Privacy page'), ('projects', 'Projects page'), ('skills', 'Skills page'), ('soloproj', 'Solo project page'), ('terms', 'Terms page')], max_length=20, verbose_name='Источник оценки')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Имя')),
                ('mail', models.CharField(blank=True, max_length=150, verbose_name='Email')),
                ('rate_value', models.IntegerField(blank=True, verbose_name='Оценка')),
                ('rate_message', models.CharField(blank=True, max_length=500, verbose_name='Сообщение')),
                ('project_version', models.CharField(max_length=10, verbose_name='Версия приложения')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Отзыв о качестве',
                'verbose_name_plural': 'Отзывы о качестве',
            },
        ),
    ]
