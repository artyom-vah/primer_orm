from django.urls import path
from .views import index, category, post_detail

urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:slug>/', category, name='category'),
    path('<int:post_id>/', post_detail, name='post_detail'),
]
