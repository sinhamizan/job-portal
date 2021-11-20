# Generated by Django 3.0.1 on 2020-06-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0024_auto_20200511_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_apply',
            name='job_recruiter_email',
            field=models.EmailField(default='mizan@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job_apply',
            name='job_seeker_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='job_apply',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
