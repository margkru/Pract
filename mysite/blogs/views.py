from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

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
    model = Blog
    fields = '__all__'

    def get_success_url(self):
        return reverse('blogs:detail_blog', kwargs={'pk': self.object.pk})

class BlogDelete(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:index')

class BlogUpdate(generic.UpdateView):
    model = Blog
    fields = '__all__'

    def get_success_url(self):
        return reverse('blogs:detail_blog', kwargs={'pk': self.object.pk})

class PostCreate(generic.CreateView):
    model = Post
    fields = '__all__'

    def get_success_url(self):
        return reverse('blogs:detail_post', kwargs={'pk': self.object.pk})

class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blogs:index')

class PostUpdate(generic.UpdateView):
    model = Post
    fields = '__all__'

    def get_success_url(self):
        return reverse('blogs:detail_post', kwargs={'pk': self.object.pk})
