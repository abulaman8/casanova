from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.contrib.auth.models import User





# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    curlat = models.FloatField(blank=True, null=True)
    curlong = models.FloatField(blank=True, null=True)


    def __str__(self) -> str:
        return self.user.username

@receiver(signal=post_save, sender=Student)
def student_post_save_handler(sender, instance, created, *args, **kwargs):
    if not created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("admin_room", 
                {
                    "type": "chat_message", 
                    "lattitude": instance.curlat,
                    "longitude": instance.curlong
                }
            )
    
@receiver(post_save, sender = User)
def user_creation_handler(sender, instance, created, *args, **kwargs):
    Student.objects.create(
        user = instance,
    )