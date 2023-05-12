from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from django.shortcuts import get_object_or_404

from expenses_control.api.utils import inline_serializer

from expenses_control.authentication.services import auth_knox_token_create
from expenses_control.users.models import User


class UserLoginEmailPasswordLoginApi(APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

    class OutputSerializer(serializers.Serializer):
        user = inline_serializer(fields={
            "id": serializers.IntegerField(),
            "username": serializers.CharField(),
            "email": serializers.EmailField(),
        })
        token = serializers.CharField()

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated_data = input_serializer.validated_data

        user = get_object_or_404(User, email=validated_data["email"])

        if not user.check_password(validated_data["password"]):
            return Response(status=status.HTTP_404_NOT_FOUND)

        token = auth_knox_token_create(user=user)

        output_serializer = self.OutputSerializer({
            "user": user,
            "token": token,
        })

        return Response(data=output_serializer.data)
