# Generated by Django 4.0.2 on 2022-03-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default='Cape Town, South Africa', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.TextField(default='(021) 234-5678', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='tel',
            field=models.TextField(default='(021) 234-5678', max_length=100),
        ),
    ]
