# Generated by Django 3.1.1 on 2021-02-21 04:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]