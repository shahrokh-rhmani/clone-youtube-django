from PIL import Image
from django.db import models
from studio.models import Channel
from django.urls import reverse


class Video(models.Model):
    channel = models.ForeignKey(Channel, null=True, blank=True, related_name="videos", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    path = models.URLField(max_length=200, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    number_of_views = models.BigIntegerField(default=0)
    img = models.ImageField(upload_to='videos/images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detailview', kwargs={'ch_name': self.channel.channel_name, 'video_id': self.id})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            img = Image.open(self.img.path)
            output_size = (625, 350)  # Set desired width and height
            img = img.resize(output_size, Image.LANCZOS)
            img.save(self.img.path)