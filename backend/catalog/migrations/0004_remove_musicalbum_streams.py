# Generated by Django 4.2.5 on 2023-11-10 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_albumstreaming'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicalbum',
            name='streams',
        ),
    ]