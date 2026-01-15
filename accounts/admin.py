from django.contrib import admin
from .models import OAuthClient, AuthorizationCode, OAuthToken

@admin.register(OAuthClient)
class OAuthClientAdmin(admin.ModelAdmin):
    list_display = ("name", "client_id", "is_active", "created_at")
    readonly_fields = ("client_id", "created_at")

@admin.register(AuthorizationCode)
class AuthorizationCodeAdmin(admin.ModelAdmin):
    list_display = ("user", "client", "expires", "is_used")
    readonly_fields = ("code", "created_at")

@admin.register(OAuthToken)
class OAuthTokenAdmin(admin.ModelAdmin):
    list_display = ("user", "client", "access_token_expires_at", "is_revoked")
    readonly_fields = ("access_token", "refresh_token", "created_at")

