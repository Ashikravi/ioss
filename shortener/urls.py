from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analytics/', views.analytics, name='analytics'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
]
