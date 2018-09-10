from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BudgetModel, ExpenseModel, IncomeModel, MiniExpenseModel

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class BudgetForm(forms.ModelForm):
    name = forms.CharField(label='Budget Name', max_length=30)

    class Meta:
        model = BudgetModel
        fields = ['name']


class IncomeForm(forms.ModelForm):
    name = forms.CharField(label = 'Income Name', max_length=30)
    amount = forms.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        model = IncomeModel
        fields = ['name', 'amount']


class ExpenseForm(forms.ModelForm):
    name = forms.CharField(label = 'Expense Name', max_length=30)
    amount = forms.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        model = ExpenseModel
        fields = ['name', 'amount']


class MiniExpenseForm(forms.ModelForm):
    name = forms.CharField(label = 'Mini expense name', max_length = 30)
    amount = forms.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        model = MiniExpenseModel
        fields = ['name', 'amount']
