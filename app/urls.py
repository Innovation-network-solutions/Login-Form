from django.urls import path

from app import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('', views.my_login, name='login'),
    path('logout/', views.logout, name='logout'),
]
