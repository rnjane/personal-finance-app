from django.views.generic import ListView
from .models import BudgetModel, IncomeModel, ExpenseModel, MiniExpenseModel

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


class IncomeController(ListView):
    def create_income(request, budget_id, income_name, income_amount):
        income = IncomeModel(budget_id = budget_id, name = income_name, amount = income_amount)
        income.save()
        incomes = IncomeModel.objects.filter(budget_id=budget_id)
        return(incomes)

    def view_all_incomes(request, budget_id):
        incomes = IncomeModel.objects.filter(budget_id = budget_id)
        return(incomes)

    def edit_income(request, budget_id, income_id, income_new_name, income_new_amount):
        income = IncomeModel.objects.filter(pk=income_id)
        income.update(name=income_new_name, amount=income_new_amount)
        incomes = IncomeModel.objects.filter(budget_id = budget_id)
        return(incomes)

    def delete_income(request, budget_id, income_id):
        income =    IncomeModel.objects.filter(pk=income_id)
        income.delete()
        incomes = IncomeModel.objects.filter(budget_id = budget_id)
        return(incomes)


class ExpenseController(ListView):
    def view_all_expenses(request, budget_id):
        expenses = ExpenseModel.objects.filter(budget_id = budget_id)
        return(expenses)

    def create_expense(request, budget_id, expense_name, expense_amount):
        expense = ExpenseModel(budget_id = budget_id, name = expense_name, amount = expense_amount)
        expense.save()
        expenses = ExpenseModel.objects.filter(budget_id = budget_id)
        return(expenses)

    def edit_expense(request, budget_id, expense_id, expense_new_name, expense_new_amount):
        expense = ExpenseModel.objects.filter(pk = expense_id)
        expense.update(name=expense_new_name, amount=expense_new_amount)
        expenses = ExpenseModel.objects.filter(budget_id = budget_id)
        return(expenses)

    def delete_expense(request, budget_id, expense_id):
        expense = ExpenseModel.objects.filter(pk=expense_id)
        expense.delete()
        expenses = ExpenseModel.objects.filter(budget_id = budget_id)
        return(expenses)


class MiniExpenseController(ListView):
    def view_all_mini_expense(request, expense_id):
        mini_expenses = MiniExpenseModel.objects.filter(expense_id=expense_id)
        return(mini_expenses)

    def create_mini_expense(request, expense_id, mini_expense_name, mini_expense_amount):
        mini_expense = MiniExpenseModel(expense_id = expense_id, name = mini_expense_name, amount = mini_expense_amount)
        mini_expense.save()
        mini_expenses = MiniExpenseModel.objects.filter(expense_id = expense_id)
        return(mini_expenses)


    def edit_mini_expense(request, expense_id, mini_expense_id, new_mini_expense_name, new_mini_expense_amount):
        mini_expense = MiniExpenseModel.objects.filter(pk = mini_expense_id)
        mini_expense.update(name=new_mini_expense_name, amount=new_mini_expense_amount)
        mini_expenses = MiniExpenseModel.objects.filter(expense_id = expense_id)
        return(mini_expenses)

    def delete_mini_expense(request, expense_id, mini_expense_id):
        mini_expense = MiniExpenseModel.objects.filter(pk = mini_expense_id)
        mini_expense.delete()
        mini_expenses = MiniExpenseModel.objects.filter(expense_id = expense_id)
        return(mini_expenses)