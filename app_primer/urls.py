from django.urls import path
# from .views import index, category_posts, post_detail, profile
from .views import AllPosts, CategoryPosts, PostDetail, contacti

app_name = 'app_primer'

urlpatterns = [
    path('', AllPosts.as_view(), name='all_posts'),
    path('contacti/', contacti, name='contacti'),
    path('category/<slug:slug>/', CategoryPosts.as_view(), name='category'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    # path('profile/<str:username>/', Profile.as_view(), name='profile')
]
