from django.shortcuts import render


def register(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'budgets.html')

def budget(request):
    return render(request, 'budget-page.html')
