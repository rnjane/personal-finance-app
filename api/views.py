from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api import serializers
from fapp import budgets
from rest_framework.views import APIView

# class Register(APIView):
#     permission_classes = (AllowAny, )
#     def post(self, request):
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password1 = request.data.get('password1')
#         password2 = request.data.get('password2')
#         if username is None or email is None or password1 is None or password2 is None:
#             return Response({'error': 'Please provide all the required credentials'},
#                         status=status.HTTP_400_BAD_REQUEST)
#         else:
#             new_user = 
#         if password1 == password2:


class Login(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
        else:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},
                    status=status.HTTP_200_OK)


class Budgets(APIView):
    def get(self, request, format=None):
        budgets_list = budgets.Budget.index(request)
        serializer = serializers.BudgetSerializer(budgets_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        response = budgets.Budget.create_budget_controller(request, request.data)
        serializer = serializers.BudgetSerializer(response, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        response = budgets.Budget.edit_budget_controller(request, new_name=request.data.get('new_name'), budget_id=request.data.get('budget_id'))
        serializer = serializers.BudgetSerializer(response, many=True)
        return Response(serializer.data)

    def delete(self, request, format=None):
        response = budgets.Budget.delete_budget_controller(request, budget_id=request.data.get('budget_id'))
        serializer = serializers.BudgetSerializer(response, many=True)
        return Response(serializer.data)


class Incomes(APIView):
    def get(self, request, format=None):
        incomes_list = budgets.IncomeController.view_all_incomes(request, budget_id=request.data.get('budget_id'))
        serializer = serializers.IncomeSerializer(incomes_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        response = budgets.IncomeController.create_income(request, budget_id=request.data.get('budget_id'), income_name=request.data.get('income_name'), income_amount=request.data.get('income_amount'))
        serializer = serializers.IncomeSerializer(response, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        response = budgets.IncomeController.edit_income(request, budget_id=request.data.get('budget_id'), income_id=request.data.get('income_id'), income_new_name=request.data.get('income_new_name'), income_new_amount=request.data.get('income_new_amount'))
        serializer = serializers.IncomeSerializer(response, many=True)
        return Response(serializer.data)

    def delete(self, request, format=None):
        response = budgets.IncomeController.delete_income(request, budget_id=request.data.get('budget_id'), income_id=request.data.get('income_id'))
        serializer = serializers.IncomeSerializer(response, many=True)
        return Response(serializer.data)


class Expenses(APIView):
    def get(self, request, format=None):
        expenses_list = budgets.ExpenseController.view_all_expenses(request, budget_id=request.data.get('budget_id'))
        serializer = serializers.ExpenseSerializer(expenses_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        response = budgets.ExpenseController.create_expense(request, budget_id=request.data.get('budget_id'), expense_name=request.data.get('expense_name'), expense_amount=request.data.get('expense_amount'))
        serializer = serializers.ExpenseSerializer(response, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        response = budgets.ExpenseController.edit_expense(request, budget_id=request.data.get('budget_id'), expense_id=request.data.get('expense_id'), expense_new_name=request.data.get('expense_new_name'), expense_new_amount=request.data.get('expense_new_amount'))
        serializer = serializers.ExpenseSerializer(response, many=True)
        return Response(serializer.data)

    def delete(self, request, format=None):
        response = budgets.ExpenseController.delete_expense(request, budget_id=request.data.get('budget_id'), expense_id=request.data.get('expense_id'))
        serializer = serializers.ExpenseSerializer(response, many=True)
        return Response(serializer.data)


class MiniExpenses(APIView):
    def get(self, request, format=None):
        mini_expenses_list = budgets.MiniExpenseController.view_all_mini_expense(request, expense_id=request.data.get('expense_id'))
        serializer = serializers.MiniExpenseSerializer(mini_expenses_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        response = budgets.MiniExpenseController.create_mini_expense(request, expense_id=request.data.get('expense_id'), mini_expense_name=request.data.get('mini_expense_name'), mini_expense_amount=request.data.get('mini_expense_amount'))
        serializer = serializers.MiniExpenseSerializer(response, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        response = budgets.MiniExpenseController.edit_mini_expense(request, expense_id=request.data.get('expense_id'), mini_expense_id=request.data.get('mini_expense_id'), new_mini_expense_name=request.data.get('mini_expense_new_name'), new_mini_expense_amount=request.data.get('mini_expense_new_amount'))
        serializer = serializers.MiniExpenseSerializer(response, many=True)
        return Response(serializer.data)

    def delete(self, request, format=None):
        response = budgets.MiniExpenseController.delete_mini_expense(request, expense_id=request.data.get('expense_id'), mini_expense_id=request.data.get('mini_expense_id'))
        serializer = serializers.MiniExpenseSerializer(response, many=True)
        return Response(serializer.data)

