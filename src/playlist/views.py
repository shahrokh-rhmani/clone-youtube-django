from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from video.models import Video
from .models import Playlist, PlaylistItem
from .forms import PlaylistForm, PlaylistItemForm


@login_required
def playlist_list(request):
    playlists = Playlist.objects.filter(channel__user=request.user)
    return render(request, 'playlist_list.html', {'playlists': playlists})


@login_required
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id, channel__user=request.user)
    return render(request, 'playlist_detail.html', {'playlist': playlist})


@login_required
def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            return redirect('playlist_list')
    else:
        form = PlaylistForm()
    return render(request, 'create_playlist.html', {'form': form})


@login_required
def add_to_playlist(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        playlist_id = request.POST.get('playlist')
        action = request.POST.get('action')
        playlist = get_object_or_404(Playlist, id=playlist_id, channel__user=request.user)
        
        if action == 'add':
            playlist_item, created = PlaylistItem.objects.get_or_create(playlist=playlist, video=video)
            if created:
                return JsonResponse({'success': True, 'action': 'added'})
            else:
                return JsonResponse({'success': False, 'error': 'Video already in playlist'}, status=400)
        elif action == 'remove':
            playlist_item = PlaylistItem.objects.filter(playlist=playlist, video=video).first()
            if playlist_item:
                playlist_item.delete()
                return JsonResponse({'success': True, 'action': 'removed'})
            else:
                return JsonResponse({'success': False, 'error': 'Video not in playlist'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
