from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.shortcuts import get_object_or_404

from knox.models import AuthToken

from . import serializers

from .models import User


class UserGetMeApi(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        user = request.user

        output_serializer = serializers.UserSerializer(user)

        return Response(data=output_serializer.data)


class UserLoginEmailPasswordLoginApi(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        input_serializer = serializers.UserLoginEmailPasswordSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated_data = input_serializer.validated_data

        user = get_object_or_404(User, email=validated_data["email"])

        if not user.check_password(validated_data["password"]):
            return Response(status=status.HTTP_404_NOT_FOUND)

        token = AuthToken.objects.create(user=user)[1]

        response = {
            "user": serializers.UserSerializer(user).data,
            "token": token,
        }

        return Response(data=response)

