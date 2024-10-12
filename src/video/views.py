from django.shortcuts import render, get_object_or_404
from studio.models import Channel
from interaction.models import Like, Dislike
from .models import Video
from django.http import HttpResponseNotFound


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

    if not Channel.objects.filter(channel_name=ch_name).exists():
        return HttpResponseNotFound("Channel does not exist")

    context = {
        'video': video,
        'user_liked': user_liked,
        'user_disliked': user_disliked,
    }
    return render(request, 'detailview.html', context)
