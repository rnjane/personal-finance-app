from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, NewBudgetForm, EditBudgetForm
from .models import Budget

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'budgets.html', {'budgets': budgets})

def create_budget(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        form = NewBudgetForm(request.POST or None)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user_id = request.user.id
            budget.name = form.cleaned_data['name']
            budget.amount = form.cleaned_data['amount']
            budget.save()
            return redirect('index')
        print(form.errors)

def budget(request):
    return render(request, 'budget-page.html')

def edit_budget(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        form = EditBudgetForm(request.POST)
        if form.is_valid():
            budget = Budget.objects.get(pk=budget_id)
            budget.name = form.cleaned_data['name']
            budget.amount = form.cleaned_data['amount']
            budget.save()
            return redirect('index')

def delete_budget(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        budget = Budget.objects.get(pk=budget_id)
        budget.delete()
        budgets = Budget.objects.filter(user=request.user)
        return redirect('index')
