from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class BudgetModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    total_income = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    total_expenses = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    def remaining_amount(self):
        if self.total_expenses == None:
            return 100
        return ((self.total_income - self.total_expenses) / self.total_income) * 100

    class Meta:
        ordering = ['date_created']


class ExpenseModel(models.Model):
    budget = models.ForeignKey(BudgetModel, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    remaining_amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    def rem_amount(self):
        if self.remaining_amount == None:
            return 100
        return self.remaining_amount

    class Meta:
        ordering = ['date_created']


class IncomeModel(models.Model):
    budget = models.ForeignKey(BudgetModel, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created']


class MiniExpenseModel(models.Model):
    expense = models.ForeignKey(ExpenseModel, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created']
