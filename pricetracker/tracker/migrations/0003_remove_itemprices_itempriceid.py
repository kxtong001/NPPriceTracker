# Generated by Django 4.1 on 2022-09-04 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20220904_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemprices',
            name='itempriceID',
        ),
    ]
