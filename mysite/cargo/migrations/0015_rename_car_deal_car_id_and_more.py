# Generated by Django 5.0.6 on 2024-07-05 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0014_rename_car_id_deal_car_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deal',
            old_name='car',
            new_name='car_id',
        ),
        migrations.RenameField(
            model_name='deal',
            old_name='supplier',
            new_name='supplier_id',
        ),
    ]
