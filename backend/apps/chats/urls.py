from django.urls import path

from .api.views import ChatsView, ChatView
from .api.views.messages import ChatMessagesView, ChatMessageView

urlpatterns = [
    path('', ChatsView.as_view(), name='chats'),
    path('<int:chat_id>', ChatView.as_view(), name='chat'),
    path('<int:chat_id>/messages', ChatMessagesView.as_view(), name='chat_messages'),
    path('<int:chat_id>/messages/<int:message_id>', ChatMessageView.as_view(), name='chat_message')
]