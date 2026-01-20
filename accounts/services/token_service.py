import uuid
from datetime import timedelta
from django.utils import timezone
from accounts.models import OAuthClient, OAuthToken
from accounts.services.authorization_code_service import (
    validate_authorization_code,
    mark_authorization_code_used,
)

def issue_tokens(authorization_code, client_id, client_secret):
    try:
        client = OAuthClient.objects.get(
            client_id=client_id,
            client_secret=client_secret,
            is_active=True,
        )
    except OAuthClient.DoesNotExist:
        return None, "Invalid client credentials"

    auth_code = validate_authorization_code(authorization_code, client)
    if not auth_code:
        return None, "Invalid or expired authorization code"

    access_token = uuid.uuid4().hex
    refresh_token = uuid.uuid4().hex
    access_token_expires_at = timezone.now() + timedelta(hours=1)

    token = OAuthToken.objects.create(
        user=auth_code.user,
        client=client,
        access_token=access_token,
        refresh_token=refresh_token,
        access_token_expires_at=access_token_expires_at,
    )

    mark_authorization_code_used(auth_code)

    return token, None
