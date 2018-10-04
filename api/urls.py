from django.conf.urls import url
from django.contrib.auth import views as auth_views
from api import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name='api-login'),
    url(r'^budgets/$', views.Budgets.as_view(), name='budgets_api'),
    url(r'^expenses/$', views.Expenses.as_view(), name='expenses_api'),
    url(r'^incomes/$', views.Incomes.as_view(), name='incomes_api'),
    url(r'^mini-expenses/$', views.MiniExpenses.as_view(), name='mini_expenses_api'),
]