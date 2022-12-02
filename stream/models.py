from hashlib import sha256
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Camera(models.Model):
    cam_id = models.CharField(max_length=8, null=True, blank=True, unique=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    liveurl = models.URLField(blank=True, null= True)


    def __str__(self) -> str:
        return self.cam_id



@receiver(signal=post_save, sender=Camera)
def cam_post_save_handler(created, instance, sender, *args, **kwargs):
    if not instance.cam_id:
        instance.cam_id = str(sha256(str(instance.id).encode('utf-8')).hexdigest())[:8]
        instance.save()

