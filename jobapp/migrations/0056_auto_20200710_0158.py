# Generated by Django 3.0.1 on 2020-07-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0055_auto_20200710_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_cv_traning',
            name='training_year',
            field=models.CharField(max_length=30),
        ),
    ]