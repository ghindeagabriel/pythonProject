# Generated by Django 2.1.7 on 2019-04-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proiect_licenta', '0024_auto_20190429_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('CELE_MAI_NOI_STIRI', 'Cele mai noi stiri'), ('FOTBAL', 'Fotbal'), ('TENIS', 'Tenis'), ('STIRI_EXTERNE', 'Stiri externe'), ('HANDBAL', 'Handbal')], default='Fotbal', max_length=200),
        ),
    ]
