from rest_framework import serializers
from django.contrib.auth.models import User 
from fapp.models import BudgetModel, ExpenseModel, IncomeModel, MiniExpenseModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class BudgetSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = BudgetModel
        fields = ('id', 'user', 'name', 'total_income', 'total_expenses', 'date_created', 'date_modified')


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeModel
        fields = ('budget', 'name', 'amount', 'date_created')


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseModel
        fields = ('budget', 'name', 'amount', 'remaining_amount', 'date_created')


class MiniExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniExpenseModel
        fields = ('expense', 'name', 'amount', 'date_created')