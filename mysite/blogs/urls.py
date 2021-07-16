from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog<int:pk>/', views.DetailBlogView.as_view(), name='detail_blog'),
    path('post<int:pk>/', views.DetailPostView.as_view(), name='detail_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
