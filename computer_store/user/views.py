from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


# Create your views here.
class GetAllUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # queryset = User.objects.all()
        # serializer_class = serializers.GetAllUserSerializer
        return Response({"message": "auuu"})
