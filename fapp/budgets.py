from django.views.generic import ListView
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, NewBudgetForm, EditBudgetForm, NewMiniBudgetForm, EditMiniBudgetForm
from .models import BudgetModel, MiniBudgetModel

class Budget(ListView):
    def index(request):
        budgets = BudgetModel.objects.filter(user=request.user)
        return(budgets)

    def create_budget(request, name, amount):
        budget = BudgetModel(user_id=request.user.id, name=name, amount=amount)
        budget.save()
        budgets = BudgetModel.objects.filter(user=request.user)
        return(budgets)

    def edit_budget(request, budget_id, new_name, new_amount):
        budget = BudgetModel.objects.get(pk=budget_id)
        budget.name = new_name
        budget.amount = new_amount
        budget.save()
        budgets = BudgetModel.objects.filter(user=request.user)
        return(budgets)

    def delete_budget(request, budget_id):
        budget = BudgetModel.objects.get(pk=budget_id)
        budget.delete()
        budgets = BudgetModel.objects.filter(user=request.user)
        return(budgets)
