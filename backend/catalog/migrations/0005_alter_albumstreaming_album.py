# Generated by Django 4.2.5 on 2023-11-10 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_musicalbum_streams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumstreaming',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streams', to='catalog.musicalbum'),
        ),
    ]