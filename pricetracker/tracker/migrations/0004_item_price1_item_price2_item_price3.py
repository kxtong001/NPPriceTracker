# Generated by Django 4.1 on 2022-09-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_remove_itemprices_itempriceid'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='price2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='price3',
            field=models.FloatField(default=0),
        ),
    ]
