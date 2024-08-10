from django.db import models

class AudioAttachment(models.Model):
    src = models.TextField()
    
    class Meta:
        db_table = 'audio_attachments'