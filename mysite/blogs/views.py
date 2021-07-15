from django.shortcuts import get_object_or_404, render
from .models import Blog, Post

def index(request):
    latest_blogs_list = Blog.objects.all()
    context = { 'latest_blogs_list': latest_blogs_list}
    return render(request, 'blogs/index.html', context)

def detail_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail_blog.html', {'blog': blog})

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blogs/detail_post.html', {'post': post})
