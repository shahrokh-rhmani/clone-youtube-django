from django.db import models
from studio.models import Channel
from video.models import Video


class Playlist(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PlaylistItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name="playlist_items", on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['playlist', 'video'], name='unique_playlist_video')
        ]

    def __str__(self):
        return f'{self.playlist.title} - {self.video.title}'
    

class WatchLater(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('channel', 'video')
        
    def __str__(self):
        return f'{self.channel.channel_name} - {self.video.title}'


