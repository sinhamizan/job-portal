# Generated by Django 3.0.1 on 2020-07-07 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0034_job_apply_recruiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_view', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Post')),
                ('jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Recruiter_Register')),
            ],
        ),
    ]
