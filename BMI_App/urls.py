from django.urls import path
from . import views

urlpatterns = [
     path('registerUser/', views.registerUser, name='registerUser'),
     
     path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
     path('myAccount/', views.myAccount, name='myAccount'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('calculator/', views.calculator, name='calculator'),
     path('result/', views.result, name='result'),
]

