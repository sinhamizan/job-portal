# Generated by Django 3.0.1 on 2020-07-09 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0053_auto_20200710_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_cv_academic_qualification',
            name='duration',
            field=models.CharField(default='---', max_length=50),
        ),
    ]
