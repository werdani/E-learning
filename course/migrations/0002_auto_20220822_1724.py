# Generated by Django 3.2.13 on 2022-08-22 15:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student_course_name',
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, related_name='enroll', to=settings.AUTH_USER_MODEL),
        ),
    ]
