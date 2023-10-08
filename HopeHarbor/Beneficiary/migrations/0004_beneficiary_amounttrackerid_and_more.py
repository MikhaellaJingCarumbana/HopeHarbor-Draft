# Generated by Django 4.2.6 on 2023-10-08 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0003_alter_dik_diktype'),
        ('Beneficiary', '0003_alter_beneficiary_needs'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='AmountTrackerID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Donor.amount_tracker'),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='GoodsTrackerID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Donor.goods_tracker'),
        ),
    ]
