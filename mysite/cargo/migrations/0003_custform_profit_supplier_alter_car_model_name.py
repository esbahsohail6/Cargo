# Generated by Django 5.0.6 on 2024-06-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0002_alter_car_body_style_alter_car_car_dimension_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('NIC', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('profit', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supp_name', models.CharField(max_length=100)),
                ('supp_email', models.CharField(max_length=100)),
                ('supp_address', models.CharField(max_length=100)),
                ('supp_phoneno', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='model_name',
            field=models.CharField(max_length=100),
        ),
    ]