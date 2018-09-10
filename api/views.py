from rest_framework import viewsets
from .serializers import BudgetSerializer, MiniBudgetSerializer
from fapp.models import Budget, MiniBudget
from fapp import views

