from rest_framework import serializers

class AuthorizationRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    client_id = serializers.UUIDField()