# Generated by Django 4.2 on 2024-02-04 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentoro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalpropertytransactiontype',
            name='transaction_type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
