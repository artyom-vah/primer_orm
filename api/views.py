from rest_framework import viewsets
from .serializers import PostSerializer, CategorySerializer
from app_primer.models import User, Category, Post, Comment, Follow


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
