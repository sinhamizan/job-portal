# Generated by Django 3.0.1 on 2020-04-27 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0005_auto_20200427_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_salary', models.CharField(max_length=10)),
                ('cv', models.FileField(upload_to='')),
                ('job_seeker_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Post')),
            ],
        ),
    ]