# # Generated by Django 5.0.6 on 2024-07-05 16:02

# import django.db.models.deletion
# from django.db import migrations, models


# class Migration(migrations.Migration):

#     dependencies = [
#         ('cargo', '0012_alter_deal_car_id_alter_deal_supplier_id'),
#     ]

#     operations = [
#         migrations.AlterField(
#             model_name='deal',
#             name='car_id',
#             field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargo.car'),
#         ),
#         migrations.AlterField(
#             model_name='deal',
#             name='supplier_id',
#             field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargo.supplier'),
#         ),
#         migrations.AlterField(
#             model_name='sales',
#             name='car_id',
#             field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.car'),
#         ),
#         migrations.AlterField(
#             model_name='sales',
#             name='cust_id',
#             field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.custform'),
#         ),
#         migrations.AlterField(
#             model_name='sales',
#             name='supplier_id',
#             field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.supplier'),
#         ),
#     ]
