# Generated by Django 5.0.2 on 2024-03-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kifalat', '0021_alter_progress_amount_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='amount_paid',
            field=models.DecimalField(blank=True, decimal_places=2, default='N/A', max_digits=10, null=True),
        ),
    ]
