# Generated by Django 3.0.4 on 2020-03-30 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_item_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Item_Price',
            field=models.FloatField(),
        ),
    ]
