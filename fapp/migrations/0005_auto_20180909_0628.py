# Generated by Django 2.0.7 on 2018-09-09 06:28

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0004_auto_20180909_0557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgetmodel',
            options={},
        ),
        migrations.AlterField(
            model_name='budgetmodel',
            name='total_expenses',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='budgetmodel',
            name='total_income',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='expensemodel',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='expensemodel',
            name='remaining_amount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='incomemodel',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20),
        ),
    ]