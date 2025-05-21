from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'), 
    path('users/', views.users, name='users') , 
    path('<int:user_id>/', views.user_detail, name='user_detail') , 
    path('users/user_posts/', views.user_posts, name = 'user_posts'),
    path('users/user_posts/', views.user_post_view, name = 'user_posts_view'),
]
