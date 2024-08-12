from django.db import models

from .chats import Chat
from apps.accounts.models import User


class ChatMessage(models.Model):
    body = models.TextField(null=True)
    attachment_code = models.CharField(
            choices=[('FILE', 'FILE'), ('AUDIO', 'AUDIO')],
            max_length=10,
            null=True
        )
    attachment_id = models.IntegerField(null=True)
    
    viewed_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'chat_messages'
        
    def __str__(self):
        return f'{self.from_user} - {self.chat}: {self.created_at}'
    
    