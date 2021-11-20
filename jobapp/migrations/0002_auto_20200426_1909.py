# Generated by Django 3.0.1 on 2020-04-26 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='recruiter_register',
            name='company_name',
            field=models.CharField(default='test', max_length=120),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Job_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('salary', models.CharField(max_length=120)),
                ('prefered_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Both')], default=3, max_length=1)),
                ('vacancy', models.CharField(max_length=10)),
                ('job_description', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Category')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Recruiter_Register')),
            ],
        ),
    ]
