# Generated by Django 2.1.7 on 2019-04-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proiect_licenta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_title',
            field=models.ImageField(default='static/images/pamant.jpg', upload_to=''),
        ),
    ]
