from rest_framework import serializers

from accounts.api.serializers import UserSerializer

from attachments.api.serializers import FileAttachmentSerializer, AudioAttachmentSerializer
from attachments.models import FileAttachment, AudioAttachment

from chats.models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    from_user = serializers.SerializerMethodField()
    attachment = serializers.SerializerMethodField()
    
    class Meta:
        model = ChatMessage
        fields = ['id', 'body', 'attachment', 'from_user', 
                  'viewed_at', 'created_at']
        
    def get_from_user(self, message):
        return UserSerializer(message.from_user).data
    
    def get_attachment(self, message):
        if message.attachment_code == 'FILE':
            file_attachment = FileAttachment.objects.filter(
                    id=message.attachment_id
                ).first()
            
            if not file_attachment:
                return None
            
            return {
                'file': FileAttachmentSerializer(file_attachment).data
            }
        
        if message.attachment_code == 'AUDIO':
            audio_attachment = AudioAttachment.objects.filter(
                    id=message.attachment_id
                ).first()
            
            if not audio_attachment:
                return None
            
            return {
                'audio': AudioAttachmentSerializer(audio_attachment).data
            }
            
    