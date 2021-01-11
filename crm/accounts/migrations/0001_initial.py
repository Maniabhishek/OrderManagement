# Generated by Django 3.1.5 on 2021-01-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
