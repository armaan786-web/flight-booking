# Generated by Django 3.1.2 on 2022-06-09 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0013_auto_20201121_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled')], max_length=45),
        ),
    ]
