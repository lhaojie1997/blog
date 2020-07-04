# Generated by Django 3.0.4 on 2020-04-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20200419_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hobby',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女'), ('unknown', '保密')], default='unknown', max_length=20, verbose_name='性别'),
        ),
    ]
