# Generated by Django 2.2.9 on 2020-01-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifpy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitchGame',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('box_art_url', models.URLField()),
            ],
        ),
    ]
