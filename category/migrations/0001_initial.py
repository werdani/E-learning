<<<<<<< HEAD
# Generated by Django 3.2.13 on 2022-08-16 22:50
=======
# Generated by Django 3.2.14 on 2022-08-22 07:34
>>>>>>> cce6dda622ac49ffca6c75bd728a20c71d57f42d

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
            ],
        ),
    ]
