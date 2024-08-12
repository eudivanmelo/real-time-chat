from django.urls import path

from .api.views import ChatsView, ChatView

urlpatterns = [
    path('', ChatsView.as_view(), name='chats'),
    path('<int:chat_id>', ChatView.as_view(), name='chat'),
]