# Generated by Django 3.2.14 on 2022-08-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0003_remove_course_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ImageField(null=True, upload_to='courses/images'),
        ),
    ]