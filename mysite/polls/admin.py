from django.contrib import admin

from polls.models import Question, Response

admin.site.register(Question)
admin.site.register(Response)
