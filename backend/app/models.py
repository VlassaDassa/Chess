from django.db import models
from django.contrib.auth.models import AbstractUser




FAVORITE_COLOR = (
    ('white', 'white'),
    ('black','black'),
)

class User(AbstractUser):
    wins = models.IntegerField('Количество побед', default=0)
    lose = models.IntegerField('Количество поражений', default=0)
    all_games = models.IntegerField('Всего игр', default=0)
    favorite_color = models.CharField('Любимый цвет', choices=FAVORITE_COLOR, max_length=20, default='white')

    def __str__(self):
        return str(self.username)
    


WINNER_CHOICES = (
    ('draw','draw'),
    ('white', 'white'),
    ('black','black'),
)

#Структура moves
default_moves = {
            "white": [
                {
                    "number_move": 1,
                    "move": "e4 e5",

                },
            ],
            "black": [
                {
                    "number_move": 1,
                    "move": "e4 e5",

                },
            ]
        }

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game')
    game_name = models.CharField('Название игры', max_length=50, default='New game')
    moves = models.JSONField('Ходы', default=default_moves)
    winner = models.CharField('Победитель', max_length=10, choices=WINNER_CHOICES, default='draw')
    analysis = models.TextField('Анализ', max_length=500, blank=True, null=True)
    count_moves = models.IntegerField('Кол-во ходов', default=0)
    count_mistakes = models.IntegerField('Кол-во ошибок', default=0)

    def __str__(self):
        return str(self.game_name)



class Advice(models.Model):
    advice_title = models.CharField('Заголовок', max_length=40)
    advice_text = models.TextField('Текст', max_length=300)

    def __str__(self):
        return str(self.advice_title)
