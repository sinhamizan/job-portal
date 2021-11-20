# Generated by Django 3.0.1 on 2020-07-09 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0047_create_cv_academic_qualification_create_cv_add_referance_create_cv_basic_info_create_cv_job_experien'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_cv_academic_qualification',
            name='cv_jobseeker',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_cv_add_referance',
            name='cv_jobseeker',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_cv_basic_info',
            name='cv_jobseeker',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_cv_job_experience',
            name='cv_jobseeker',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_cv_language_profiency',
            name='cv_jobseeker',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_cv_traning',
            name='cv_jobseeker',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='jobapp.Job_Seeker_Register'),
            preserve_default=False,
        ),
    ]