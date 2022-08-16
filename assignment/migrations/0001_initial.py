# Generated by Django 3.2.13 on 2022-08-07 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.FloatField()),
                ('upload_assign', models.FileField(max_length=254, upload_to=None)),
                ('assignment_student', models.ManyToManyField(related_name='student', to=settings.AUTH_USER_MODEL)),
                ('assignment_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='video.video')),
            ],
        ),
    ]
