# Generated by Django 3.0.4 on 2020-04-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_hobby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.PositiveIntegerField(),
        ),
    ]
