from datetime import timedelta

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=30)
    publish_date = models.DateField('date published')

    def was_published_recently(self):
        now = timezone.now().date()
        return now - timedelta(days=1) <= self.publish_date \
               <= now + timedelta(days=1)

    def __str__(self):
        return self.question_text


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.CharField(max_length=30)
    nb_vote = models.IntegerField()

    def __str__(self):
        return self.response_text
