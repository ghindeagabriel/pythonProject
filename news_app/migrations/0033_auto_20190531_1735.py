# Generated by Django 2.1.7 on 2019-05-31 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proiect_licenta', '0032_auto_20190531_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
