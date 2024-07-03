from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.Users.as_view(), name='users'),
    path('user/<id>', views.Users.as_view(), name='user'),

    path('users_games/', views.UsersWithGames.as_view(), name='users_game'),
    path('user_games/<id>', views.UsersWithGames.as_view(), name='user_game'),

    path('games/', views.Games.as_view(), name='games'),
    path('game/<id>', views.Games.as_view(), name='game'),

    path('games_user/', views.GamesWithUser.as_view(), name='games_user'),
    path('game_user/<id>', views.GamesWithUser.as_view(), name='games_user'),
]




