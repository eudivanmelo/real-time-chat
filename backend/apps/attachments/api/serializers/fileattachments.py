from apps.attachments.models import FileAttachment
from apps.attachments.utils import Formatter

from rest_framework import serializers

from django.conf import settings


class FileAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAttachment
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['size'] = Formatter.format_bytes(instance.size)
        representation['src'] = f'{settings.CURRENT_URL}{instance.src}'
        
        return representation