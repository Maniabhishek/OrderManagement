# Generated by Django 3.1.5 on 2021-01-10 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210110_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='slug',
        ),
    ]
