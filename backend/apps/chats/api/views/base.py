from rest_framework.views import APIView

from django.db.models import Q
from django.utils.timezone import now

from apps.accounts.models import User

from apps.chats.models import Chat, ChatMessage
from apps.chats.utils.exceptions import UserNotFound, ChatNotFound
from apps.chats.api.serializers import ChatSerializer

class BaseView(APIView):
    """
    Base view for all chat related views.
    """
    
    def get_user(self, raise_exception=True, **kwargs) -> User | None:
        """
        Get user by given kwargs.
        
        Args:
            raise_exception (bool, optional): Raise UserNotFound exception if user is not found. Defaults to True.
            **kwargs: Keyword arguments to filter user by.
        
        Returns:
            User | None: User object if found, otherwise None.
        """
        user = User.objects.filter(**kwargs).first()
        
        if not user and raise_exception:
            raise UserNotFound
        
        return user

    def has_existing_chat(self, user_id, to_user) -> Chat | None:
        """
        Check if a chat exists between two users.
        
        Args:
            user_id (int): ID of the first user.
            to_user (int): ID of the second user.
        
        Returns:
            Chat | None: Chat object if found, otherwise None.
        """
        chat = Chat.objects.filter(
            (Q(from_user=user_id) & Q(to_user=to_user)) |
            (Q(from_user=to_user) & Q(to_user=user_id)),
            deleted_at__isnull=True
        ).first()
        
        if chat:
            return ChatSerializer(chat, context={'user_id': user_id}).data
        
    def chat_belongs_to_user(self, chat_id, user_id) -> Chat | None:
        """
        Check if a chat belongs to a given user.
        
        Args:
            chat_id (int): ID of the chat.
            user_id (int): ID of the user.
        
        Returns:
            Chat | None: Chat object if found, otherwise None.
        
        Raises:
            ChatNotFound: If chat is not found.
        """
        chat = Chat.objects.filter(
            Q(from_user=user_id) | Q(to_user=user_id),
            id=chat_id,
            deleted_at__isnull=True
        ).first()
        
        if not chat:
            raise ChatNotFound
        
        return chat
    
    def mark_messages_as_seen(self, chat_id, user_id) -> None:
        """
        Mark all unseen messages in a chat as seen for a given user.
        
        Args:
            chat_id (int): ID of the chat.
            user_id (int): ID of the user.
        """
        ChatMessage.objects.filter(
            chat_id=chat_id,
            viewed_at__isnull=True,
            deleted_at__isnull=True
        ).exclude(
            from_user=user_id
        ).update(
            viewed_at=now()
        )
