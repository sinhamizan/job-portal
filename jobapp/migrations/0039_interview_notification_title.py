# Generated by Django 3.0.1 on 2020-07-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0038_remove_create_interview_jobseeker'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview_notification',
            name='title',
            field=models.CharField(default='new', max_length=120),
            preserve_default=False,
        ),
    ]
