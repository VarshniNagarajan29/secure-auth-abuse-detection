from django.utils import timezone
from accounts.models import AuthorizationCode

def validate_authorization_code(code, client):
    try:
        auth_code = AuthorizationCode.objects.filter(code=code).first()
    except AuthorizationCode.DoesNotExist:
        return None

    if auth_code.client != client:
        return None

    if auth_code.expires < timezone.now():
        return None

    if auth_code.is_used:
        return None

    return auth_code


def mark_authorization_code_used(auth_code):
    auth_code.is_used = True
    auth_code.save(update_fields=['is_used'])