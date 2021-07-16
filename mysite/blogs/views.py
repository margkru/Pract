from django.views import generic
from django.views.generic import CreateView

from .models import Blog, Post

class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_blogs_list'

    def get_queryset(self):
        return Blog.objects.all()


class DetailBlogView(generic.DetailView):
    model = Blog
    template_name = 'blogs/detail_blog.html'

class DetailPostView(generic.DetailView):
    model = Post
    template_name = 'blogs/detail_post.html'

class BlogCreate(generic.CreateView):
    pass

class BlogDelete(generic.DeleteView):
    pass

class BlogUpdate(generic.UpdateView):
    pass

class PostCreate(generic.CreateView):
    pass

class PostDelete(generic.DeleteView):
    pass

class PostUpdate(generic.UpdateView):
    pass
