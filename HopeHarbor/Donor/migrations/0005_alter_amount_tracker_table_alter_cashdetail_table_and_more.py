# Generated by Django 4.2.6 on 2023-10-09 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0004_rename_cashdetails_cashdetail_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='amount_tracker',
            table='amount_tracker',
        ),
        migrations.AlterModelTable(
            name='cashdetail',
            table='cashdetails',
        ),
        migrations.AlterModelTable(
            name='currency',
            table='currency',
        ),
        migrations.AlterModelTable(
            name='dik',
            table='dik',
        ),
        migrations.AlterModelTable(
            name='donor',
            table='donor',
        ),
        migrations.AlterModelTable(
            name='goods_tracker',
            table='goods_tracker',
        ),
        migrations.AlterModelTable(
            name='goodsdetail',
            table='goodsdetails',
        ),
    ]
