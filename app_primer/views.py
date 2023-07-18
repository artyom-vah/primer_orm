from django.shortcuts import render
from .models import Post, Category, User


# Create your views here.
def index(request):
    posts = Post.objects.all()
    all_users = User.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'all_users': all_users,
        'categories': categories,
    }
    return render(request, 'app_primer/index.html', context)


def category(request, slug):
    category_posts = Post.objects.filter(categories__slug=slug)
    quantity = Post.objects.filter(categories__slug=slug).count()
    context = {
        'category_posts': category_posts,
        'quantity': quantity,
    }
    return render(request, 'app_primer/category.html', context)

def post_detail(request, post_id):
    post = Post.objects.filter(pk=post_id)[0]
    context = {
        'post': post,
    }
    return render(request, 'app_primer/post_detail.html', context)
