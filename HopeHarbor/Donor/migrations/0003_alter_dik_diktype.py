# Generated by Django 4.2.6 on 2023-10-08 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0002_alter_dik_gdid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dik',
            name='DikType',
            field=models.CharField(choices=[('food', 'Food'), ('clothing', 'Clothing'), ('shelter', 'Shelter'), ('education', 'Education'), ('medical', 'Medical'), ('utilities', 'Utilities'), ('transportation', 'Transportation'), ('employment', 'Employment'), ('other', 'Other')], default='food', max_length=50),
        ),
    ]
