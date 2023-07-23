from django.urls import path
from .views import register, profile
from django.contrib.auth import views

urlpatterns = [
    path('reg/', register, name='reg'),
    path('profile/', profile, name='profile'),
    path('user/', views.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', views.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
]
