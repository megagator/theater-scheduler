# Generated by Django 4.0.1 on 2022-01-23 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(editable=False, max_length=134, unique=True),
        ),
    ]