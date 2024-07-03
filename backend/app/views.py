from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Count

from . import serializers
from . import models



class Users(APIView):
    def get_queryset(self, id=None):
        if id:
            return models.User.objects.get(pk=id)
        return models.User.objects.all()

    def get(self, request, id=None):
        queryset = self.get_queryset(id)
        data = serializers.UserSerializer(queryset, many=not bool(id)).data
        return Response(data, status=status.HTTP_200_OK)
    

class UsersWithGames(APIView):
    def get_queryset(self, id=None):
        if id:
            return models.User.objects.get(pk=id)
        return models.User.objects.all().prefetch_related('game')
    
    def get(self, request, id=None):
        queryset = self.get_queryset(id)
        data = serializers.UserWithGameSerializer(queryset, many=not bool(id)).data
        return Response(data, status=status.HTTP_200_OK)
    

class Games(APIView):
    def get_queryset(self, id=None):
        if id:
            return models.Game.objects.get(pk=id)
        return models.Game.objects.all()

    def get(self, request, id=None):
        queryset = self.get_queryset(id)
        data = serializers.GameSerializer(queryset, many=not bool(id)).data
        return Response(data, status=status.HTTP_200_OK)
    

class GamesWithUser(APIView):
    def get_queryset(self, id=None):
        if id:
            return models.Game.objects.get(pk=id)
        return models.Game.objects.all().select_related('user')

    def get(self, request, id=None):
        queryset = self.get_queryset(id)
        data = serializers.GameWithUserSerializer(queryset, many= not bool(id)).data
        return Response(data, status=status.HTTP_200_OK)