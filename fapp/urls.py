from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views, budgets

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),

    url(r'^$', views.index, name='index'),
    url(r'^create-budget/$', views.create_budget, name='create_budget'),
    url(r'^(?P<budget_id>[0-9]+)/edit-budget/$', views.edit_budget, name='edit_budget'),
    url(r'^(?P<budget_id>[0-9]+)/delete-budget/$', views.delete_budget, name='delete_budget'),

    url(r'^(?P<budget_id>[0-9]+)/income/$', views.create_income, name='create_income'),
    url(r'^(?P<budget_id>[0-9]+)/incomes/$', views.view_all_incomes, name='view_incomes'),
    url(r'^(?P<budget_id>[0-9]+)/income/(?P<income_id>[0-9]+)/edit-income/$', views.edit_income, name='edit_income'),
    url(r'^(?P<budget_id>[0-9]+)/income/(?P<income_id>[0-9]+)/delete-income/$', views.delete_income, name='delete_income'),

    url(r'^(?P<budget_id>[0-9]+)/expense/$', views.create_expense, name='create_expense'),
    url(r'^(?P<budget_id>[0-9]+)/expenses/$', views.view_all_expenses, name='view_expenses'),
    url(r'^(?P<budget_id>[0-9]+)/expense/(?P<expense_id>[0-9]+)/edit_expense/$', views.edit_expense, name='edit_expense'),
    url(r'^(?P<budget_id>[0-9]+)/expense/(?P<expense_id>[0-9]+)/delete_expense/$', views.delete_expense, name='delete_expense'),

    url(r'^(?P<expense_id>[0-9]+)/mini-expense/$', views.create_mini_expense, name='create_mini_expense'),
    url(r'^(?P<expense_id>[0-9]+)/mini-expenses/$', views.view_all_mini_expenses, name='view_mini_expenses'),
    url(r'^(?P<expense_id>[0-9]+)/mini-expense/(?P<mini_expense_id>[0-9]+)/edit-mini-expense/$', views.edit_mini_expense, name='edit_mini_expense'),
    url(r'^(?P<expense_id>[0-9]+)/mini-expense/(?P<mini_expense_id>[0-9]+)/delete-mini-expense/$', views.delete_mini_expense, name='delete_mini_expense'),
]