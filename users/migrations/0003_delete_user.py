# Generated by Django 4.2.1 on 2023-10-14 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]