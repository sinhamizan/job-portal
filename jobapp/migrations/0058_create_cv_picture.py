# Generated by Django 3.0.1 on 2020-07-10 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0057_auto_20200710_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_CV_Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='avatar.png', upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cv_jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register')),
            ],
            options={
                'verbose_name': 'CV Singature',
                'verbose_name_plural': 'CV Singatures',
            },
        ),
    ]
