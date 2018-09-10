from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, BudgetForm, IncomeForm, ExpenseForm, MiniExpenseForm
from .budgets import Budget, IncomeController, ExpenseController, MiniExpenseController
from .models import BudgetModel, ExpenseModel


def is_authenticated(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

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
    budgets = Budget.index(request)
    return render(request, 'budgets.html', {'budgets': budgets})

def create_budget(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        form = BudgetForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            Budget.create_budget_controller(request, name)
            return redirect('index')
        else:
            return redirect('index', errors = form.errors)

def edit_budget(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        form = BudgetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mid = budget_id
            Budget.edit_budget_controller(request, mid, name)
            return redirect('index')

def delete_budget(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        Budget.delete_budget_controller(request, budget_id)
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

def create_income(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        form = IncomeForm(request.POST or None)
        if form.is_valid():
            IncomeController.create_income(budget_id, form.cleaned_data['name'], form.cleaned_data['amount'])
            return redirect('incomes')

def view_all_incomes(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        incomes = IncomeController.view_all_incomes(budget_id)
        budget = get_object_or_404(BudgetModel, pk=budget_id)
        return render(request, 'incomes.html', {'incomes': incomes, 'budget': budget})

def edit_income(request, budget_id, income_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        form = IncomeForm(request.POST or None)
        IncomeController.edit_income(budget_id, income_id, form.cleaned_data['newname'], form.cleaned_data['newamount'])
        return redirect('incomes')

def delete_income(request, budget_id, income_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        IncomeController.delete_income(budget_id, income_id)
        return redirect('incomes')

def create_expense(request, budget_id):
    if is_authenticated(request):
        form = ExpenseForm(request.POST or None)
        ExpenseController.create_expense(budget_id, form.cleaned_data['name'], form.cleaned_data['amount'])
        return redirect('expenses')

def view_all_expenses(request, budget_id):
    if is_authenticated(request):
        expenses = ExpenseController.view_all_expenses(budget_id)
        budget = get_object_or_404(BudgetModel, pk=budget_id)
        return render(request, 'expenses.html', {'expenses': expenses, 'budget': budget})

def edit_expense(request, budget_id, expense_id):
    if is_authenticated(request):
        form = ExpenseForm(request.POST or None)
        ExpenseController.edit_expense(budget_id, expense_id, form.cleaned_data['newname'], form.cleaned_data['newamount'])
        return redirect('expenses')

def delete_expense(request, budget_id, expense_id):
    if is_authenticated(request):
        ExpenseController.delete_expense(budget_id, expense_id)
        return redirect('expenses')

def create_mini_expense(request, expense_id):
    if is_authenticated(request):
        form = MiniExpenseForm(request.POST or None)
        MiniExpenseController.create_mini_expense(expense_id, form.cleaned_data['name'], form.cleaned_data['amount'])
        return redirect('mini-expenses')

def view_all_mini_expenses(request, expense_id):
    if is_authenticated(request):
        mini_expenses = MiniExpenseController.view_all_mini_expense(expense_id)
        expense = get_object_or_404(ExpenseModel, pk=expense_id)
        return render(request, 'mini-expenses.html', {'mini-expenses': mini_expenses, 'expense': expense})

def edit_expense(request, expense_id, mini_expense_id):
    if is_authenticated(request):
        form = MiniExpenseForm(request.POST or None)
        MiniExpenseController.edit_mini_expense(expense_id, mini_expense_id, form.cleaned_data['newname'], form.cleaned_data['newamount'])
        return redirect('mini-expenses')

def delete_expense(request, mini_expense_id):
    if is_authenticated(request):
        MiniExpenseController.delete_mini_expense(mini_expense_id)
        return redirect('mini-expenses')

