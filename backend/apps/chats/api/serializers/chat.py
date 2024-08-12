from rest_framework import serializers

from apps.accounts.api.serializers import UserSerializer

from apps.chats.models import Chat, ChatMessage
from apps.chats.api.serializers.chatmessage import ChatMessageSerializer

from apps.attachments.models import FileAttachment, AudioAttachment
from apps.attachments.api.serializers import FileAttachmentSerializer, AudioAttachmentSerializer

class ChatSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    unseen_count = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()
    
    class Meta:
        model = Chat
        fields = ['id', 'last_message', 'unseen_count', 'user', 'viewed_at', 'created_at']
        
    def get_user(self, chat):
        user = chat.from_user
        
        if user.id == self.context['user_id']:
            user = chat.to_user
            
        return UserSerializer(user).data
    
    def get_unseen_count(self, chat):
        unsseen_count = ChatMessage.objects.filter(
                chat_id=chat.id,
                viewed_at__isnull=True,
                deleted_at__isnull=True
            ).exclude(
                from_user=self.context['user_id']
            ).count()
        
        return unsseen_count
    
    def get_last_message(self, chat):
        last_message = ChatMessage.objects.filter(
                chat_id=chat.id,
                deleted_at__isnull=True
            ).order_by('-created_at').first()
        
        if not last_message:
            return None
        
        return ChatMessageSerializer(last_message).data
    

