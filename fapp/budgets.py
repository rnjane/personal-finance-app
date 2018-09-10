from django.views.generic import ListView
from .models import BudgetModel

class Budget(ListView):
    def index(request):
        budgets = BudgetModel.objects.filter(user=request.user)
        return(budgets)

    def create_budget_controller(request, name):
        budget = BudgetModel(user_id=request.user.id, name=name)
        budget.save()
        budgets = BudgetModel.objects.filter(user=request.user)
        return(budgets)

    def edit_budget_controller(request, budget_id, new_name):
        budget = BudgetModel.objects.get(pk=budget_id)
        budget.name = new_name
        budget.save()
        budgets = BudgetModel.objects.filter(user=request.user)
        return(budgets)

    def delete_budget_controller(request, budget_id):
        budget = BudgetModel.objects.get(pk=budget_id)
        budget.delete()
        budgets = BudgetModel.objects.filter(user=request.user)
        return(budgets)
