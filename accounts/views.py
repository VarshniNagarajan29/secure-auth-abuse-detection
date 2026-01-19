from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import AuthorizationRequestSerializer
from accounts.services.authorization_services import authorize_user


class OAuthAuthorizeView(APIView):
    def post(self, request):
        serializer = AuthorizationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        auth_code, error = authorize_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            client_id=serializer.validated_data['client_id'],
        )

        if error:
            return Response({'detail': error}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"authorization_code": auth_code.code, "expires_in":60}, status=status.HTTP_200_OK)