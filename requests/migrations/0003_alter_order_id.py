# Generated by Django 4.1.5 on 2023-02-06 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_rename_request_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]