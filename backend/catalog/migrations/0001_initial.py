# Generated by Django 4.2.5 on 2023-09-20 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('artist', models.CharField(max_length=250, verbose_name='Artist')),
                ('year', models.SmallIntegerField(verbose_name='Year')),
                ('wiki_url', models.URLField(null=True, verbose_name='WikiPedia')),
                ('spotify_url', models.URLField(null=True, verbose_name='Spotify')),
                ('apple_url', models.URLField(null=True, verbose_name='Apple Music')),
                ('youtube_url', models.URLField(null=True, verbose_name='YouTube')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
