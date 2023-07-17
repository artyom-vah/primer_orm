from rest_framework import serializers

from app_primer.models import User, Category, Post, Comment, Follow


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    categories = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'pub_date', 'author', 'categories')


