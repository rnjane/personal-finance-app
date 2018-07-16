from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.FloatField()

    def __str__(self):
        return self.name


class MiniBudget(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.FloatField()

    def __str__(self):
        return self.name