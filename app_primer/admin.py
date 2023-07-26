from django.contrib import admin
from .models import Category, Post, Comment, Follow


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    list_filter = ('title', 'slug', 'description')
    search_fields = ('title', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date', 'author', 'categories')
    list_filter = ('title', 'text', 'pub_date', 'author', 'categories')
    search_fields = ('title', 'text', 'pub_date', 'author', 'categories')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text')
    list_filter = ('post', 'author', 'text')
    search_fields = ('post', 'author', 'text')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    list_filter = ('user', 'author')
    search_fields = ('user', 'author')
