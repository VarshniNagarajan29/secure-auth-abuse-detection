from rest_framework import serializers

class AuthorizationRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    client_id = serializers.UUIDField()


class TokenRequestSerializer(serializers.Serializer):
    authorization_code = serializers.CharField()
    client_id = serializers.UUIDField()
    client_secret = serializers.CharField(write_only=True)
