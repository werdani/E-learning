# Generated by Django 3.2.13 on 2022-08-16 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='grades',
            field=models.FloatField(null=True),
        ),
    ]
