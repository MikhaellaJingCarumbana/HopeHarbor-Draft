# Generated by Django 4.2.6 on 2023-10-10 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0007_alter_cashdetail_donorid'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='Username',
            field=models.CharField(default='', max_length=30),
        ),
    ]