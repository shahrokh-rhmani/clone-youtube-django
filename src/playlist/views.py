from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Playlist


@login_required
def playlist_list(request):
    playlists = Playlist.objects.filter(channel__user=request.user)
    return render(request, 'playlist_list.html', {'playlists': playlists})


@login_required
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id, channel__user=request.user)
    return render(request, 'playlist_detail.html', {'playlist': playlist})