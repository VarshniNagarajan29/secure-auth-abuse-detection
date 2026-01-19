import uuid
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import authenticate
from accounts.models import OAuthClient, AuthorizationCode


def authorize_user(username, password, client_id):
    try:
        client = OAuthClient.objects.get(client_id=client_id, is_active=True)
    except OAuthClient.DoesNotExist:
        return None, "Invalid credentials"

    user = authenticate(username=username, password=password)
    if not user:
        return None, "Invalid credentials"

    code = uuid.uuid4().hex
    expires = timezone.now() + timedelta(minutes=1)

    auth_code = AuthorizationCode.objects.create(
        code=code,
        user=user,
        client=client,
        expires=expires,
    )

    return auth_code, None