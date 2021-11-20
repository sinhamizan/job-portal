# Generated by Django 3.0.1 on 2020-04-30 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0020_recruiter_register_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='prefered_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Male & Female')], default=3, max_length=1),
        ),
        migrations.AlterField(
            model_name='recruiter_register',
            name='picture',
            field=models.FileField(default='sample.png', upload_to=''),
        ),
    ]