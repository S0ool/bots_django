# Generated by Django 5.0.6 on 2024-06-10 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='slug',
        ),
    ]