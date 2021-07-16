from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog<int:pk>/', views.DetailBlogView.as_view(), name='detail_blog'),
    path('post<int:pk>/', views.DetailPostView.as_view(), name='detail_post'),
    path('blog/create/', views.BlogCreate.as_view(), name='create'),
    path('blog<int:pk>/update/', views.BlogUpdate.as_view(), name='update'),
    path('blog<int:pk>/delete/', views.BlogDelete.as_view(), name='delete'),
    path('post/create/', views.PostCreate.as_view(), name='create'),
    path('post<int:pk>/update/', views.PostUpdate.as_view(), name='update'),
    path('post<int:pk>/delete/', views.PostDelete.as_view(), name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
