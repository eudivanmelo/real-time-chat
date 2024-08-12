from apps.attachments.models import AudioAttachment

from rest_framework import serializers

from django.conf import settings


class AudioAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioAttachment
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['src'] = f'{settings.CURRENT_URL}{instance.src}'
        
        return representation