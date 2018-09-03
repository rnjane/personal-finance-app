from django.db import models
from django.contrib.auth.models import User

class BudgetModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.FloatField()

    def __str__(self):
        return self.name


class MiniBudgetModel(models.Model):
    budget = models.ForeignKey(BudgetModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.FloatField()

    def __str__(self):
        return self.name