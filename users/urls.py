from django.urls import path
from .views import register

urlpatterns = [
    path('reg/', register, name='reg'),
]
