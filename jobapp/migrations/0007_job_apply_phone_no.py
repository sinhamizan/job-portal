# Generated by Django 3.0.1 on 2020-04-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_job_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_apply',
            name='phone_No',
            field=models.CharField(default='0216547', max_length=20),
            preserve_default=False,
        ),
    ]
