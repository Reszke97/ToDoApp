from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import (
    IsAuthenticated, 
    AllowAny
)
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework import filters


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddToDo(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        dane = request.data
        dane["user_id"] = request.user.id
        serializer = AddToDoSerializer(data=dane)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        if request.user.is_anonymous:
            return HttpResponse('<html style="max-height:41px"><body><pre style="word-wrap: break-word; white-space: pre-wrap;">{"detail":"Authentication credentials were not provided."}</pre></body></html>', status=401)
        else:
            queryset = Task.objects.filter(user_id=user_id)
            serializer = AddToDoSerializer(queryset, many = True)
            return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        user_id = request.user.id
        try:
            data = Task.objects.get(id=request.query_params.get('id'))
            if data.user_id == user_id:
                data.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        user_id = request.user.id
        try:
            data = Task.objects.get(id=request.query_params.get('id'))
            if data.user_id == user_id:
                serializer = AddToDoSerializer(data, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        user_id = request.user.id
        try:
            data = Task.objects.get(id=request.query_params.get('id'))
            if data.user_id == user_id:
                if data.isDone == True:
                    data.isDone = False
                else:
                    data.isDone = True
                data.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetTask(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        try:
            data = Task.objects.get(id=request.query_params.get('id'))
            if data.user_id == user_id:
                serializer = AddToDoSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SearchTasks(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        queryset = Task.objects.filter(user_id=user_id).filter(isDone=request.query_params.get('isDone'))
        serializer = AddToDoSerializer(queryset, many = True)
        return Response(serializer.data)


    


 
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer

class CustomTokenVerifyView(TokenVerifyView):
    permission_classes = [AllowAny]
    serializer_class = TokenVerifySerializer


# Logout
class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny,]
    # authentication_classes = ()

    def post(self, request):
        try:
            if request.data["refresh_token"] is not None:
                refresh_token = request.data["refresh_token"]
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response(status=status.HTTP_205_RESET_CONTENT)
            else:
                return Response('Pusty token', status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
