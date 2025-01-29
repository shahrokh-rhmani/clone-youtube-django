from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from video.models import Video
from .models import Comment, Dislike, Like



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


def comment_view(request):
    if request.method == 'POST':
        video_id = request.POST.get('video', False)
        comment_text = request.POST.get('text', False)
        parent_id = request.POST.get('parent', False)

        if not video_id or not comment_text:
            return JsonResponse({'bool': False, 'error': 'Video ID and text are required.'}, status=400)

        parent_comment = get_object_or_404(Comment, id=parent_id) if parent_id else None

        Comment.objects.create(
            video_id=video_id,
            user=request.user,
            text=comment_text,
            parent=parent_comment
        )
        
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False, 'error': 'Invalid request method.'}, status=405)
