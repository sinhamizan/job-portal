# Generated by Django 3.0.1 on 2020-04-28 00:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0011_auto_20200428_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_post',
            name='job_deadline',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
