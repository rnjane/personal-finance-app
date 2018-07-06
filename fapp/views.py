from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, NewBudgetForm
from django.http import HttpResponseRedirect

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
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'budgets.html')

def create_budget(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        form = NewBudgetForm(request.POST or None)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user_id = request.user.id
            budget.name = form.cleaned_data['name']
            budget.amount = form.cleaned_data['amount']
            budget.save()
            return render(request, 'budget-page.html', {'budget': budget})
        print(form.errors)

def budget(request):
    return render(request, 'budget-page.html')
