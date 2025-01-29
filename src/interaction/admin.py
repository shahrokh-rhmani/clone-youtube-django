from django.contrib import admin
from .models import Like, Dislike, Comment


admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Comment)
