from django.shortcuts import render, get_object_or_404
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


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category_posts = category.posts.all()
    # quantity = Post.objects.filter(categories__slug=slug).count()
    context = {
        'category_posts': category_posts,
        # 'quantity': quantity,
    }
    return render(request, 'app_primer/category.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'app_primer/post_detail.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts_author = author.posts.all()
    context = {
        'author': author,
        'posts_author': posts_author
    }
    return render(request, 'app_primer/profile.html', context)
