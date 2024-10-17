from django.contrib import admin
from .models import Playlist, PlaylistItem

admin.site.register(Playlist)
admin.site.register(PlaylistItem)
