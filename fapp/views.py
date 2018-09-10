from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, BudgetForm, IncomeForm, ExpenseForm, MiniExpenseForm
from .budgets import Budget

# from finance.settings import BASE_DIR, STATIC_ROOT, STATIC_URL, STATICFILES_DIRS

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

# def create_mini_budget(request, budget_id):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     else:
#         form = NewMiniBudgetForm(request.POST or None)
#         if form.is_valid():
#             budget = get_object_or_404(Budget, pk=budget_id)
#             mini_budget = form.save(commit=False)
#             mini_budget.budget = budget
#             mini_budget.name = form.cleaned_data['name']
#             mini_budget.amount = form.cleaned_data['amount']
#             mini_budget.save()
#             return redirect('budget', budget_id)

def incomes_view(request, budget_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        # print('\n', BASE_DIR, '\n', STATIC_ROOT, '\n', STATIC_URL, '\n', STATICFILES_DIRS)
        # budget = get_object_or_404(Budget, pk=budget_id)
        # mini_budgets = MiniBudget.objects.filter(budget = budget_id)
        # return render(request, 'budget-page.html', {'mini_budgets': mini_budgets, 'budget': budget})
        return render(request, 'incomes.html')

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

# def edit_mini_budget(request, budget_id, mini_budget_id):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     else:
#         form = EditMiniBudgetForm(request.POST)
#         if form.is_valid():
#             mini_budget = MiniBudget.objects.get(id=mini_budget_id)
#             mini_budget.name = form.cleaned_data['name']
#             mini_budget.amount = form.cleaned_data['amount']
#             mini_budget.save()
#             return redirect('budget', budget_id)
#
# def delete_mini_budget(request, budget_id, mini_budget_id):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     else:
#         mini_budget = MiniBudget.objects.get(pk=mini_budget_id)
#         mini_budget.delete()
#         return redirect('budget', budget_id)