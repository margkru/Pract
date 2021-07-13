from django.db import models


class Blog(models.Model):
    post_header = models.CharField(max_length=200)
    post_text = models.Field()
    post_img = models.ImageField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_header
