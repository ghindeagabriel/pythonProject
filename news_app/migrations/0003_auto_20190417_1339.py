# Generated by Django 2.1.7 on 2019-04-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proiect_licenta', '0002_post_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_title',
            field=models.ImageField(default='static/images/pamant.jpg', upload_to='images/'),
        ),
    ]
