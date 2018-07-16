from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, NewBudgetForm, EditBudgetForm, NewMiniBudgetForm, EditMiniBudgetForm
from .models import Budget, MiniBudget

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

def create_mini_budget(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        form = NewMiniBudgetForm(request.POST or None)
        if form.is_valid():
            budget = get_object_or_404(Budget, pk=budget_id)
            mini_budget = form.save(commit=False)
            mini_budget.budget = budget
            mini_budget.name = form.cleaned_data['name']
            mini_budget.amount = form.cleaned_data['amount']
            mini_budget.save()
            return redirect('budget', budget_id)

def budget(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        budget = get_object_or_404(Budget, pk=budget_id)
        mini_budgets = MiniBudget.objects.filter(budget = budget_id)
        return render(request, 'budget-page.html', {'mini_budgets': mini_budgets, 'budget': budget})

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

def edit_mini_budget(request, budget_id, mini_budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        form = EditMiniBudgetForm(request.POST)
        if form.is_valid():
            mini_budget = MiniBudget.objects.get(id=mini_budget_id)
            mini_budget.name = form.cleaned_data['name']
            mini_budget.amount = form.cleaned_data['amount']
            mini_budget.save()
            return redirect('budget', budget_id)

def delete_mini_budget(request, budget_id, mini_budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        mini_budget = MiniBudget.objects.get(pk=mini_budget_id)
        mini_budget.delete()
        return redirect('budget', budget_id)