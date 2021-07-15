from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog<int:blog_id>/', views.detail_blog, name='detail_blog'),
    path('post<int:post_id>', views.detail_post, name='detail_post'),
]