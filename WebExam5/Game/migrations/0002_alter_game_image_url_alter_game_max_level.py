# Generated by Django 4.1.7 on 2023-03-10 13:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='game',
            name='max_level',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Max Level'),
        ),
    ]
