# Generated by Django 5.0.3 on 2024-05-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='moves',
            field=models.JSONField(default={'black': [{'move': 'e4 e5', 'number_move': 1}], 'white': [{'move': 'e4 e5', 'number_move': 1}]}, verbose_name='Ходы'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorite_color',
            field=models.CharField(choices=[('white', 'white'), ('black', 'black')], default='white', max_length=20, verbose_name='Любимый цвет'),
        ),
    ]
