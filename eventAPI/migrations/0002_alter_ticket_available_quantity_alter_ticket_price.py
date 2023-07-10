# Generated by Django 4.2.3 on 2023-07-10 21:23

from django.db import migrations, models
import eventAPI.validators


class Migration(migrations.Migration):

    dependencies = [
        ('eventAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='available_quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, validators=[eventAPI.validators.AllowPositiveDecimalValuesOnly]),
        ),
    ]