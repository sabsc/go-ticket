# Generated by Django 2.0 on 2018-04-27 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theaters', '0002_remove_movie_releasedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='showtime',
            name='theater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='theaters.Theater'),
        ),
    ]
