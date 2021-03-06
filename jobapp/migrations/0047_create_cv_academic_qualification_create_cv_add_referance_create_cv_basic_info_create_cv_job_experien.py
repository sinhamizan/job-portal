# Generated by Django 3.0.1 on 2020-07-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0046_auto_20200709_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_CV_Academic_Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=120)),
                ('major', models.CharField(max_length=120)),
                ('Institute', models.CharField(max_length=250)),
                ('passing_year', models.DateField()),
                ('cgpa', models.FloatField()),
                ('duration', models.FloatField(blank=True, default='---', null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Job Post',
                'verbose_name_plural': 'Job Posts',
            },
        ),
        migrations.CreateModel(
            name='Create_CV_Add_Referance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('designation', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('company_location', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('mobile', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'CV Job Referance',
                'verbose_name_plural': 'CV Job Referances',
            },
        ),
        migrations.CreateModel(
            name='Create_CV_Basic_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(blank=True, max_length=30, null=True)),
                ('father_name', models.CharField(blank=True, max_length=120, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=120, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('marrige_status', models.CharField(blank=True, max_length=50, null=True)),
                ('nationalilty', models.CharField(blank=True, max_length=100, null=True)),
                ('nid', models.IntegerField(blank=True, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('current_address', models.TextField(blank=True, null=True)),
                ('parmanant_address', models.TextField(blank=True, null=True)),
                ('career_objective', models.TextField(blank=True, null=True)),
                ('skill_and_specialize', models.TextField(blank=True, null=True)),
                ('hobby', models.TextField(blank=True, null=True)),
                ('signiture', models.ImageField(default='sign.png', upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'CV Basic Info',
                'verbose_name_plural': 'CV Basic Infos',
            },
        ),
        migrations.CreateModel(
            name='Create_CV_Job_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=120)),
                ('company_name', models.CharField(max_length=200)),
                ('company_location', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_still_work', models.BooleanField(verbose_name=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'CV Job Experience',
                'verbose_name_plural': 'CV Job Experiences',
            },
        ),
        migrations.CreateModel(
            name='Create_CV_Language_Profiency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=120)),
                ('profiency', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'CV Language Profiency',
                'verbose_name_plural': 'CV Language Profiencies',
            },
        ),
        migrations.CreateModel(
            name='Create_CV_Traning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traning_title', models.CharField(max_length=120)),
                ('topic', models.CharField(max_length=150)),
                ('training_year', models.DateField()),
                ('duration', models.CharField(max_length=50)),
                ('achievement', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'CV Traning Summary',
                'verbose_name_plural': 'CV Traning Summaries',
            },
        ),
    ]
