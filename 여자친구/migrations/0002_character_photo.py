# Generated by Django 4.2.13 on 2024-05-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('여자친구', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo/%Y/%m/%d/'),
        ),
    ]
