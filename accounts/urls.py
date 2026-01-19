from django.urls import path
from accounts.views import OAuthAuthorizeView

urlpatterns = [
    path("oauth/authorize", OAuthAuthorizeView.as_view()),
]
