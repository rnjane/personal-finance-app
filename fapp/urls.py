from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^budget-detail/$', views.budget, name='budget'),
    url(r'^create-budget/$', views.create_budget, name='create_budget'),
]