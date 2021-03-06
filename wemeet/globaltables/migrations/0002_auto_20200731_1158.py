# Generated by Django 3.0.8 on 2020-07-31 06:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globaltables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardtype',
            name='boardType',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='boardtype',
            name='boardTypeId',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='role',
            name='roleId',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)]),
        ),
    ]
