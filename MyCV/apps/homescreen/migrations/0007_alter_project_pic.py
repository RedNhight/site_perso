# Generated by Django 4.2.7 on 2023-12-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homescreen', '0006_alter_project_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pic',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
