from django.urls import path
from . import views


urlpatterns = [
    path('video/<int:video_id>/like/', views.likeview, name='likeview'),
    path('video/<int:video_id>/dislike/', views.dislikeview, name='dislikeview'),
]