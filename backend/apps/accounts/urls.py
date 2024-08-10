from django.urls import path

from .views import SignInView, SignUpView, UserView

urlpatterns = [
    path('signin/', SignInView.as_view(), name='sign-in'),
    path('signup/', SignUpView.as_view(), name='sign-up'),
    path('user/', UserView.as_view(), name='user'),
]
