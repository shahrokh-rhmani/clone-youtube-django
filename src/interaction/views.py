from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from video.models import Video
from .models import Like, Dislike


@login_required
def likeview(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    # Remove dislike if it exists
    Dislike.objects.filter(user=request.user, video=video).delete()
    like, created = Like.objects.get_or_create(user=request.user, video=video)
    
    if not created:
        like.delete()
    
    return redirect(request.META.get('HTTP_REFERER', 'detailview'))


@login_required
def dislikeview(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    # Remove like if it exists
    Like.objects.filter(user=request.user, video=video).delete()
    dislike, created = Dislike.objects.get_or_create(user=request.user, video=video)
    
    if not created:
        dislike.delete()
    
    return redirect(request.META.get('HTTP_REFERER', 'detailview'))