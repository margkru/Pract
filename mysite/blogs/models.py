import datetime
from django.db import models
from django.utils import timezone

class Blog(models.Model):
    blog_header = models.CharField(max_length=200)

    def __str__(self):
        return self.blog_header

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_img = models.ImageField(upload_to='images')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


