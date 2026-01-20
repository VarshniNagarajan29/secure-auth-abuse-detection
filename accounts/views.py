from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import AuthorizationRequestSerializer
from accounts.services.authorization_services import authorize_user
from accounts.serializers import TokenRequestSerializer
from accounts.services.token_service import issue_tokens



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


class OAuthTokenView(APIView):

    def post(self, request):
        serializer = TokenRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)

        token, error = issue_tokens(
            authorization_code=serializer.validated_data["authorization_code"],
            client_id=serializer.validated_data["client_id"],
            client_secret=serializer.validated_data["client_secret"],
        )

        if error:
            return Response(
                {"detail": error},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "access_token": token.access_token,
                "refresh_token": token.refresh_token,
                "expires_in": 3600,
            },
            status=status.HTTP_200_OK,
        )
