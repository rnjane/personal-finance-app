from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Budget, MiniBudget

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewBudgetForm(forms.ModelForm):
    name = forms.CharField(label='Budget Name', max_length=30)
    amount = forms.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        model = Budget
        fields = ['name', 'amount']

class EditBudgetForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=20, decimal_places=2)
    name = forms.CharField(label='Budget Name', max_length=30)

    class Meta:
        model = Budget
        fields = ['name', 'amount']

class NewMiniBudgetForm(forms.ModelForm):
    name = forms.CharField(label='Budget Name', max_length=30)
    amount = forms.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        model = MiniBudget
        fields = ['name', 'amount']

class EditMiniBudgetForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=20, decimal_places=2)
    name = forms.CharField(label='Budget Name', max_length=30)

    class Meta:
        model = MiniBudget
        fields = ['name', 'amount']