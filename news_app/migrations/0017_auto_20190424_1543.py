# Generated by Django 2.1.7 on 2019-04-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proiect_licenta', '0016_auto_20190424_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_title',
            field=models.ImageField(default='pamant.jpg', upload_to=''),
        ),
    ]
