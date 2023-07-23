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

    # тут переопределили context_object_name = 'posts'
    # выводим не все посты а пользователя adm
    # def get_queryset(self):
    #     return Post.objects.filter(author__username='adm')


#---------------------------------------------------------------------
# def category_posts(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     category_posts = category.posts.all()
#     context = {
#         'category_posts': category_posts,
#     }
#     return render(request, 'app_primer/category.html', context)

class CategoryPosts(ListView):
    model = Category
    template_name = 'app_primer/category.html'
    context_object_name = 'category_posts'
    def get_queryset(self):
        # Получаем категорию по slug из URL-адреса
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        # Возвращаем все записи (посты), связанные с этой категорией
        return category.posts.all()


#---------------------------------------------------------------------
# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     context = {
#         'post': post,
#     }
#     return render(request, 'app_primer/post_detail.html', context)

class PostDetail(DetailView):
    model = Post
    template_name = 'app_primer/post_detail.html'



#---------------------------------------------------------------------
# def profile(request, username):
#     author = get_object_or_404(User, username=username)
#     posts_author = author.posts.all()
#     context = {
#         'author': author,
#         'posts_author': posts_author
#     }
#     return render(request, 'app_primer/profile.html', context)


class Profile(DetailView):
    model = User
    template_name = 'app_primer/profile.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object
        posts_author = author.posts.all()
        context['posts_author'] = posts_author
        return context