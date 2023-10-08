from django.db.models import Avg
from django.shortcuts import render, redirect

from WebExam5.Game.models import Game
from WebExam5.Profile.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from WebExam5.Profile.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


# Create your views here.
def home_page(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'home-page.html', context)


def create_profile(request):
    profile = get_profile()

    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'create-profile.html', context)


def dashboard_page(request):
    profile = get_profile()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games,
    }

    return render(request, 'dashboard.html', context)


def details_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    average_game_rating = Game.objects.aggregate(Avg('rating'))
    average = average_game_rating['rating__avg']

    context = {
        'profile': profile,
        'games': games,
        'average': average,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    form = EditProfileForm(instance=profile)
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    form = DeleteProfileForm(instance=profile)
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)
