# Generated by Django 5.0.6 on 2024-06-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_style',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_dimension',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='tyre_strength',
            field=models.CharField(max_length=100),
        ),
    ]
