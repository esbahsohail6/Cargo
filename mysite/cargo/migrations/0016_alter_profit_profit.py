# Generated by Django 5.0.6 on 2024-07-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0015_rename_car_deal_car_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profit',
            name='profit',
            field=models.CharField(max_length=1000000),
        ),
    ]
