# Generated by Django 3.2.13 on 2022-08-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_video_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.FileField(upload_to='./media/video'),
        ),
    ]
