# Generated by Django 4.2.6 on 2023-10-09 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0003_alter_dik_diktype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CashDetails',
            new_name='CashDetail',
        ),
        migrations.RenameModel(
            old_name='GoodsDetails',
            new_name='GoodsDetail',
        ),
    ]