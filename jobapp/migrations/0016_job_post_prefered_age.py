# Generated by Django 3.0.1 on 2020-04-29 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0015_remove_job_post_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_post',
            name='prefered_age',
            field=models.CharField(choices=[('UT', 'Under 20'), ('TT', '21-30'), ('TF', '31-40'), ('FF', '41-50'), ('AF', 'Above 50')], default=2, max_length=2),
        ),
    ]
