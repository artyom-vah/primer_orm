from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category, User


#---------------------------------------------------------------------
# def index(request):
#     posts = Post.objects.all()
#     all_users = User.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'posts': posts,
#         'all_users': all_users,
#         'categories': categories,
#     }
#     return render(request, 'app_primer/index.html', context)

class AllPosts(ListView):
    model = Post
    template_name = 'app_primer/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['posts'] = Post.objects.all() # можно и так
        context['all_users'] = User.objects.all()
        context['categories'] = Category.objects.all()
        return context
