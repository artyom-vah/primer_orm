from django.urls import path
# from .views import index, category_posts, post_detail, profile

from .views import AllPosts

app_name = 'app_primer'

urlpatterns = [
    path('', AllPosts.as_view(), name='all_posts'),

]
