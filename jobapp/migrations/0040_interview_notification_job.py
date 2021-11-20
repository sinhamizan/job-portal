# Generated by Django 3.0.1 on 2020-07-07 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0039_interview_notification_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview_notification',
            name='job',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Post'),
            preserve_default=False,
        ),
    ]