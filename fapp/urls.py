from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<budget_id>[0-9]+)/budget-detail/$', views.budget, name='budget'),
    url(r'^create-budget/$', views.create_budget, name='create_budget'),
    url(r'^(?P<budget_id>[0-9]+)/edit-budget/$', views.edit_budget, name='edit_budget'),
    url(r'^(?P<budget_id>[0-9]+)/delete-budget/$', views.delete_budget, name='delete_budget'),
    url(r'^(?P<budget_id>[0-9]+)/create-mini-budget/$', views.create_mini_budget, name='create_mini_budget'),
    url(r'^(?P<budget_id>[0-9]+)/budget-detail/(?P<mini_budget_id>[0-9]+)/edit-mini-budget/$', views.edit_mini_budget, name='edit_mini_budget'),
    url(r'^(?P<budget_id>[0-9]+)/budget-detail/(?P<mini_budget_id>[0-9]+)/delete-mini-budget/$', views.delete_mini_budget, name='delete_mini_budget'),
]