# Generated by Django 4.1.5 on 2023-03-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0005_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='browser_language',
            field=models.CharField(blank=True, max_length=100, verbose_name=''),
        ),
        migrations.AddField(
            model_name='rate',
            name='cookies',
            field=models.TextField(blank=True, max_length=5000, verbose_name=''),
        ),
        migrations.AddField(
            model_name='rate',
            name='screen_resolution',
            field=models.CharField(blank=True, max_length=100, verbose_name=''),
        ),
        migrations.AddField(
            model_name='rate',
            name='timezone',
            field=models.CharField(blank=True, max_length=100, verbose_name=''),
        ),
        migrations.AddField(
            model_name='rate',
            name='user_agent',
            field=models.CharField(blank=True, max_length=2000, verbose_name=''),
        ),
    ]
