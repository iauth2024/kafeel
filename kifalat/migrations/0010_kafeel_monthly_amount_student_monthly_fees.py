# Generated by Django 5.0.2 on 2024-03-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kifalat', '0009_studentstatusupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='kafeel',
            name='monthly_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='student',
            name='monthly_fees',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
