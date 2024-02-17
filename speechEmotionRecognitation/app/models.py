from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

# Create your models here.
class Audio(models.Model):
    title = models.CharField(max_length=100, blank=True)
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title
    

@receiver(pre_delete, sender=Audio)
def delete_file(sender, instance, **kwargs):
    # Delete the associated file when the object is deleted
    if instance.audio_file:
        if os.path.isfile(instance.audio_file.path):
            os.remove(instance.audio_file.path)