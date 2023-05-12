from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from expenses_control.api.mixins import ApiAuthMixin

from expenses_control.users.models import User


class UserGetMeApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ("id", "username", "email", "daily_limit",)

    def get(self, request):
        user = request.user

        output_serializer = self.OutputSerializer(user)

        return Response(data=output_serializer.data)
