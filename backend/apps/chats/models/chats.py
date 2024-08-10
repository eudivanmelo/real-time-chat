from django.db import models

from apps.accounts.models import User

class Chat(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Chats_from_user_id')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Chats_to_user_id')
    
    viewed_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'chats'
        
    def __str__(self):
        return f'{self.from_user} - {self.to_user}: {self.created_at}'