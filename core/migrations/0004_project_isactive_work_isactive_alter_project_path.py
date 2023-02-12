# Generated by Django 4.1.5 on 2023-02-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_project_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='Активен?'),
        ),
        migrations.AddField(
            model_name='work',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='Активен?'),
        ),
        migrations.AlterField(
            model_name='project',
            name='path',
            field=models.CharField(blank=True, max_length=200, verbose_name='Папка проекта'),
        ),
    ]
