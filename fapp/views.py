from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, BudgetForm, IncomeForm, ExpenseForm, MiniExpenseForm
from .budgets import Budget, IncomeController, ExpenseController, MiniExpenseController
from .models import BudgetModel, ExpenseModel, User
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
import decimal


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
    query = request.GET.get('q')
    if query:
        budgets = budgets.filter(name__icontains=query)
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

def create_income(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        form = IncomeForm(request.POST or None)
        if form.is_valid():
            IncomeController().create_income(budget_id, form.cleaned_data['name'], form.cleaned_data['amount'])
            return redirect('view_incomes', budget_id=budget_id)


def view_all_incomes(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        incomes = IncomeController().view_all_incomes(budget_id=budget_id)
        query = request.GET.get('q')
        if query:
            incomes = incomes.filter(name__icontains=query)
        budget = get_object_or_404(BudgetModel, pk=budget_id)
        return render(request, 'incomes.html', {'incomes': incomes, 'budget': budget})

def edit_income(request, income_id, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        form = IncomeForm(request.POST or None)
        if form.is_valid():
            IncomeController().edit_income(budget_id, income_id, form.cleaned_data['name'], form.cleaned_data['amount'])
            return redirect('view_incomes', budget_id=budget_id)

def delete_income(request, budget_id, income_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        IncomeController().delete_income(budget_id, income_id)
        return redirect('view_incomes', budget_id=budget_id)

def create_expense(request, budget_id):
    if is_authenticated(request):
        form = ExpenseForm(request.POST or None)
        if form.is_valid():
            ExpenseController().create_expense(budget_id, form.cleaned_data['name'], form.cleaned_data['amount'])
            return redirect('view_expenses', budget_id=budget_id)

def view_all_expenses(request, budget_id):
    if is_authenticated(request):
        expenses = ExpenseController().view_all_expenses(budget_id)
        query = request.GET.get('q')
        if query:
            expenses = expenses.filter(name__icontains=query)
        budget = get_object_or_404(BudgetModel, pk=budget_id)
        return render(request, 'expenses.html', {'expenses': expenses, 'budget': budget})

def edit_expense(request, budget_id, expense_id):
    if is_authenticated(request):
        form = ExpenseForm(request.POST or None)
        if form.is_valid():
            ExpenseController().edit_expense(budget_id, expense_id, form.cleaned_data['name'], form.cleaned_data['amount'])
            return redirect('view_expenses', budget_id=budget_id)

def delete_expense(request, budget_id, expense_id):
    if is_authenticated(request):
        ExpenseController().delete_expense(budget_id, expense_id)
        return redirect('view_expenses', budget_id=budget_id)

def create_mini_expense(request, expense_id):
    if is_authenticated(request):
        form = MiniExpenseForm(request.POST or None)
        if form.is_valid():
            MiniExpenseController().create_mini_expense(expense_id, form.cleaned_data['name'], form.cleaned_data['amount'])
            return redirect('view_mini_expenses', expense_id=expense_id)

def view_all_mini_expenses(request, expense_id):
    if is_authenticated(request):
        mini_expenses = MiniExpenseController().view_all_mini_expense(expense_id)
        query = request.GET.get('q')
        if query:
            mini_expenses = mini_expenses.filter(name__icontains=query)
        expense = get_object_or_404(ExpenseModel, pk=expense_id)
        return render(request, 'mini-expenses.html', {'mini_expenses': mini_expenses, 'expense': expense, 'budget': expense.budget})

def edit_mini_expense(request, expense_id, mini_expense_id):
    if is_authenticated(request):
        form = MiniExpenseForm(request.POST or None)
        if form.is_valid():
            MiniExpenseController().edit_mini_expense(expense_id, mini_expense_id, form.cleaned_data['name'], form.cleaned_data['amount'])
            return redirect('view_mini_expenses', expense_id=expense_id)

def delete_mini_expense(request, expense_id,  mini_expense_id):
    if is_authenticated(request):
        MiniExpenseController().delete_mini_expense(expense_id, mini_expense_id)
        return redirect('view_mini_expenses', expense_id=expense_id)

def dashboard(request):
    if is_authenticated:
        all_expenses = decimal.Decimal(0.0)
        all_incomes = decimal.Decimal(0.0)
        budgets = Budget.index(request)
        for budget in budgets:
            '''Return total incomes and expenses for all the budgets'''
            all_expenses += decimal.Decimal(budget.total_expenses)
            all_incomes += decimal.Decimal(budget.total_income)
        return render(request, 'budgets-dashboard.html', {'expenses': all_expenses, 'incomes': all_incomes})


class ChartData(APIView):
    def get(self, request, format=None):
        labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        budgets = Budget.index(request)
        incomes = []
        expenses = []
        months = []
        tincome = 0
        texpense = 0
        month_income_expense = {}
        for budget in budgets:
            incomes.append(budget.total_income)
            expenses.append(budget.total_expenses)
            months.append(budget.date_created.strftime("%b"))
            if budget.date_created.strftime("%b") in months:
                tincome += budget.total_income
                texpense += budget.total_expenses
                month_income_expense[budget.date_created.strftime("%b")] = [tincome, texpense]
            else:
                month_income_expense[budget.date_created.strftime("%b")] = [budget.total_income, budget.total_expenses]
        av_incomes = {}
        av_expenses = {}
        
        mons = set(labels) & set(months)
        
        for label in labels:
            if label in mons:
                av_incomes[label] = month_income_expense[label][0]
                av_expenses[label] = month_income_expense[label][1]
            else:
                av_incomes[label] = 0
                av_expenses[label] = 0
        data1 = {
                "labels": labels,
                "default": list(av_incomes.values()),
        }
        
        data2 = {
                "default": list(av_expenses.values()),
        }
        data = {'incomes': data1, 'expenses': data2}
        return Response(data)

         
class PieData(APIView):
    def get(self, request):
        budgets = Budget.index(request)
        now = datetime.datetime.now()
        expense_vals = {}
        last_month = (now.month-1 if now.month > 1 else 12)
        for budget in budgets:
            if budget.date_created.strftime("%b") == ("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()[last_month-1]):
                expenses = ExpenseController.view_all_expenses(request, budget.id)
                for expense in expenses:
                    if expense.name in expense_vals:
                        expense_vals[expense.name] += expense.amount
                    else:
                        expense_vals[expense.name] = expense.amount
        data = {
            'labels': list(expense_vals.keys()),
            'values': list(expense_vals.values()),
        }
        return Response(data)
        