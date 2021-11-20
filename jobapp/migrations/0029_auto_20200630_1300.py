# Generated by Django 3.0.1 on 2020-06-30 07:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0028_auto_20200622_1048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog_post',
            options={'verbose_name': 'Blog Post', 'verbose_name_plural': 'Blog Posts'},
        ),
        migrations.AlterModelOptions(
            name='job_apply',
            options={'verbose_name': 'Job Apply', 'verbose_name_plural': 'Job Applys'},
        ),
        migrations.AlterModelOptions(
            name='job_post',
            options={'verbose_name': 'Job Post', 'verbose_name_plural': 'Job Posts'},
        ),
        migrations.AlterModelOptions(
            name='job_seeker_register',
            options={'verbose_name': 'Job Seeker Register', 'verbose_name_plural': 'Job Seeker Registers'},
        ),
        migrations.AlterModelOptions(
            name='recruiter_register',
            options={'verbose_name': 'Recruirer Register', 'verbose_name_plural': 'Recruirer Registers'},
        ),
        migrations.AddField(
            model_name='job_apply',
            name='applying_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
