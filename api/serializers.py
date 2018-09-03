from rest_framework import serializers
from fapp.models import Budget, MiniBudget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ('id', 'name', 'amount')

class MiniBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniBudget
        fields = ('id', 'name', 'amount')