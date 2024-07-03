from rest_framework import serializers
from . import models



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'wins', 'lose', 'all_games', 'favorite_color']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = '__all__'


class GameWithUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Game
        fields = '__all__'


class UserWithGameSerializer(serializers.ModelSerializer):
    game = GameSerializer(many=True, read_only=True)

    class Meta:
        model = models.User
        fields = ['id', 'username', 'wins', 'lose', 'all_games', 'favorite_color', 'game']