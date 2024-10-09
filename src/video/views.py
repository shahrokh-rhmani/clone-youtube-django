from django.shortcuts import render, get_object_or_404
from studio.models import Channel
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

    if not Channel.objects.filter(channel_name=ch_name).exists():
        return HttpResponseNotFound("Channel does not exist")

    context = {
        'video': video,
    }
    return render(request, 'detailview.html', context)
