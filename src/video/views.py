from django.shortcuts import render
from .models import Video


def listview(request):
    most_recent_videos = Video.objects.order_by('-datetime')[:8]

    context = {
        'most_recent_videos': most_recent_videos,
    }
    
    return render(request, 'listview.html', context)
