# Generated by Django 4.1.5 on 2023-03-20 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_rateelement_retry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rateelement',
            old_name='retry',
            new_name='retry_button',
        ),
    ]
