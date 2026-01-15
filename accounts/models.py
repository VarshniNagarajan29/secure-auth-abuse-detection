import uuid

from django.conf import settings
from django.db import models

# Create your models here.
class OAuthClient(models.Model):
    name = models.CharField(max_length=100)
    client_id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    client_secret = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class AuthorizationCode(models.Model):
    code = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey(OAuthClient, on_delete=models.CASCADE)
    expires = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.code)

class OAuthToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey(OAuthClient, on_delete=models.CASCADE)
    access_token = models.TextField(unique=True)
    refresh_token = models.TextField(unique=True)
    access_token_expires_at = models.DateTimeField()
    is_revoked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -{}".format(self.user, self.client)