# Generated by Django 3.0.1 on 2020-07-09 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0049_auto_20200709_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_cv_basic_info',
            name='career_objective',
        ),
        migrations.RemoveField(
            model_name='create_cv_basic_info',
            name='hobby',
        ),
        migrations.RemoveField(
            model_name='create_cv_basic_info',
            name='signiture',
        ),
        migrations.RemoveField(
            model_name='create_cv_basic_info',
            name='skill_and_specialize',
        ),
        migrations.CreateModel(
            name='Create_CV_Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_and_specialize', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cv_jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register')),
            ],
            options={
                'verbose_name': 'CV Skill & Specialization',
                'verbose_name_plural': 'CV Skills & Specializations',
            },
        ),
        migrations.CreateModel(
            name='Create_CV_Signiture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signiture', models.ImageField(default='sign.png', upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cv_jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register')),
            ],
            options={
                'verbose_name': 'CV Singature',
                'verbose_name_plural': 'CV Singatures',
            },
        ),
        migrations.CreateModel(
            name='Create_CV_Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cv_jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register')),
            ],
            options={
                'verbose_name': 'CV Hobby & Interest',
                'verbose_name_plural': 'CV Hobbies & Interests',
            },
        ),
        migrations.CreateModel(
            name='Create_CV_Career_Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_objective', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cv_jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register')),
            ],
            options={
                'verbose_name': 'CV Career Objective',
                'verbose_name_plural': 'CV Career Objecttives',
            },
        ),
    ]
