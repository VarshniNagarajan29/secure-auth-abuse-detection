from django.urls import path
from accounts.views import OAuthAuthorizeView, OAuthTokenView

urlpatterns = [
    path("oauth/authorize", OAuthAuthorizeView.as_view()),
    path("oauth/token", OAuthTokenView.as_view()),
]
