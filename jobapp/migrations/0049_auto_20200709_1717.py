# Generated by Django 3.0.1 on 2020-07-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0048_auto_20200709_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_cv_basic_info',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='create_cv_basic_info',
            name='marrige_status',
            field=models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='create_cv_basic_info',
            name='religion',
            field=models.CharField(choices=[('I', 'Islam'), ('H', 'Hindusim'), ('K', 'Christian'), ('B', 'Boddho'), ('O', 'Others')], default=1, max_length=1),
        ),
    ]
