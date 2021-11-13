from rest_framework_api_key.models import APIKey
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.shortcuts import render
from .serializers import CustomUserSerializer
from .models import CustomUser

# Create your views here.

class CustomUserCreateAPI(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        api_key = serializer.validated_data.pop('api_key')
        serializer.save(api_key=api_key)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        api_key, key = APIKey.objects.create_key(name=request.data['email'])
        serializer.validated_data['api_key'] = api_key
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = serializer.data.copy()
        data['key'] = key
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
