from django.urls import path
# from .views import index, category_posts, post_detail, profile
from .views import AllPosts, category_posts, post_detail, profile

app_name = 'app_primer'

urlpatterns = [
    path('', AllPosts.as_view(), name='all_posts'),
    path('category/<slug:slug>/', category_posts, name='category'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('profile/<str:username>/', profile, name='profile')
]
