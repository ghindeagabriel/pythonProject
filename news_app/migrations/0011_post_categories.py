# Generated by Django 2.1.7 on 2019-04-24 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proiect_licenta', '0010_auto_20190424_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('FOTBAL', 'Fotbal'), ('TENIS', 'Tenis'), ('STIRI_EXTERNE', 'Stiri externe'), ('HANDBAL', 'Handbal')], default='Fotbal', max_length=3),
        ),
    ]
