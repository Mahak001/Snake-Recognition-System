# Generated by Django 4.2.4 on 2023-08-28 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snake_app', '0004_remove_snake_submission_date_snake_upload_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snake',
            name='upload_date',
        ),
        migrations.AddField(
            model_name='snake',
            name='caption',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
