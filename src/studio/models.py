from django.contrib.auth.models import User
from django.db import models


class Channel(models.Model):
    user = models.ForeignKey(User, related_name="channels", on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.channel_name
    
    def count_subscribers(self):
        return self.subscriptions.count()
    
    
class ChannelSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, related_name="subscriptions", on_delete=models.CASCADE)
