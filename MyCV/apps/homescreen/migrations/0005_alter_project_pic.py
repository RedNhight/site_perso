# Generated by Django 4.2.7 on 2023-12-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homescreen', '0004_alter_project_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pic',
            field=models.ImageField(height_field=1080, upload_to='', width_field=1080),
        ),
    ]
