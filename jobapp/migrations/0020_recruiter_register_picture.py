# Generated by Django 3.0.1 on 2020-04-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0019_auto_20200429_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiter_register',
            name='picture',
            field=models.FileField(default='sampla.png', upload_to=''),
            preserve_default=False,
        ),
    ]
