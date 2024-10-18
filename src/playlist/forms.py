from django import forms
from .models import Playlist, PlaylistItem



class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['channel', 'title']


class PlaylistItemForm(forms.ModelForm):
    class Meta:
        model = PlaylistItem
        fields = ['playlist']