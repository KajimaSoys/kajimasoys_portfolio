# Generated by Django 4.1.5 on 2023-02-06 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='Order',
        ),
    ]
