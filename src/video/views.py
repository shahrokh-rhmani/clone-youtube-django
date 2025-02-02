# Django core imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, JsonResponse

# Application-specific imports
from studio.models import Channel
from interaction.models import Like, Dislike, Comment
from interaction.forms import CommentForm
from playlist.models import Playlist, PlaylistItem, WatchLater
from .models import Video



def listview(request):
    most_recent_videos = Video.objects.order_by('-datetime')[:8]

    context = {
        'most_recent_videos': most_recent_videos,
    }
    
    return render(request, 'listview.html', context)


def detailview(request, ch_name, video_id):
    video = get_object_or_404(Video, id=video_id)
    user_liked = Like.objects.filter(user=request.user, video=video).exists()
    user_disliked = Dislike.objects.filter(user=request.user, video=video).exists()
    user_playlists = Playlist.objects.filter(channel__user=request.user)
    playlistitem = PlaylistItem.objects.filter(video=video_id).values_list('playlist_id', flat=True)
    user_watch_later = WatchLater.objects.filter(channel__user=request.user).values_list('video_id', flat=True)
    comments = Comment.objects.filter(video__id=video_id).order_by('-datetime')

    if not Channel.objects.filter(channel_name=ch_name).exists():
        return HttpResponseNotFound("Channel does not exist")

    context = {
        'video': video,
        'user_liked': user_liked,
        'user_disliked': user_disliked,
        'playlists': user_playlists,
        'playlistitem': playlistitem,
        'watch_later_videos': user_watch_later,
        'comments': comments,
        'form': CommentForm(),
    }
    return render(request, 'detailview.html', context)



def search(request):
    query = request.GET.get('q')
    if query:
        search_results = Video.objects.filter(title__icontains=query)
    else:
        search_results = Video.objects.none()

    results = []
    for video in search_results:
        image_url = video.img.url if video.img else '/static/images/thumbnail.jpg'
        results.append({
            'id': video.id,
            'title': video.title,
            'url': video.get_absolute_url(),
            'image_url': image_url 
        })
    

    return JsonResponse({'search_results': results})