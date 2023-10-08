from django.shortcuts import render, redirect

from WebExam5.Game.forms import CreateGameForm, DeleteGameForm
from WebExam5.Game.models import Game
from WebExam5.Profile.views import get_profile


# Create your views here.
def create_game(request):
    profile = get_profile()

    if request.method == "GET":
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'create-game.html', context)


def details_game(request, id):
    profile = get_profile()
    game = Game.objects.get(pk=id)

    context = {
        'profile': profile,
        'game': game,
    }

    return render(request, 'details-game.html', context)


def edit_game(request, id):
    profile = get_profile()
    game = Game.objects.get(pk=id)

    if request.method == 'GET':
        form = CreateGameForm(instance=game)
    else:
        form = CreateGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'edit-game.html', context)


def delete_game(request, id):
    profile = get_profile()
    game = Game.objects.get(pk=id)

    form = DeleteGameForm(instance=game)
    if request.method == "POST":
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'delete-game.html', context)
