# Generated by Django 5.0.1 on 2024-04-06 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_resume_upload_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='skills',
            field=models.TextField(default='Java'),
            preserve_default=False,
        ),
    ]
