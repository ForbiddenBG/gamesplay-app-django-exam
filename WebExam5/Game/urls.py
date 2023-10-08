from django.urls import path

from WebExam5.Game.views import create_game, details_game, edit_game, delete_game

urlpatterns = (
    path('game/create/', create_game, name='create-game'),
    path('game/details/<int:id>/', details_game, name='details-game'),
    path('game/edit/<int:id>/', edit_game, name='edit-game'),
    path('game/delete/<int:id>/', delete_game, name='delete-game'),
)