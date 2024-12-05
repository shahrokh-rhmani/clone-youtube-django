from django.db import models
from django.contrib.auth.models import User
from video.models import Video


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name="likes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'video')

    def __str__(self):
        return self.video.title


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name="dislikes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'video')

    def __str__(self):
        return self.video.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f'{self.user.username} comment: {self.text[:20]}...'
    
    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()
    
    @property
    def is_parent(self):
        return self.parent is None


