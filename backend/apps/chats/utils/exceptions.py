from rest_framework.exceptions import APIException


class UserNotFound(APIException):
    status_code = 404
    default_detail = 'User not found'
    default_code = 'user_not_found'
    

class ChatNotFound(APIException):
    status_code = 404
    default_detail = 'Chat not found or user is not a member'
    default_code = 'chat_not_found'