# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from random import randint
from models import Author, Article


# Create your views here.
def vj01(request):
    return HttpResponse("Hello World!")

def getFilmovi():
    return [
    {
    'id': 1,
    'name': 'A Clockwork Orange',
    'year': 1971,
    'poster': 'slike/aClockworkOrange.jpg',
    'director': 'Stanley Kubrick',
    'genre': 'Crime, Drama, Sci-Fi'
    },
    {
    'id': 2,
    'name': 'Blow',
    'year': 2001,
    'poster': 'slike/blow.jpg',
    'director': 'Ted Demme',
    'genre': 'Biography, Crime, Drama'
    },
    {
    'id': 3,
    'name': 'Cast Away',
    'year': 2000,
    'poster': 'slike/castAway.jpg',
    'director': 'Robert Zemeckis',
    'genre': 'Adventure, Drama, Romance'
    },
    {
    'id': 4,
    'name': 'Lord of War',
    'year': 2005,
    'poster': 'slike/lordOfWar.jpg',
    'director': 'Andrew Niccol',
    'genre': 'Crime, Drama, Thriller'
    },
    {
    'id': 5,
    'name': 'The Watchmen',
    'year': 2009,
    'poster': 'slike/watchmen.jpg',
    'director': 'Zack Snyder',
    'genre': 'Action, Drama, Mystery'
    }
    ]

def getFilmById(id):
    for film in getFilmovi():
        if(film['id'] == id):
            return film
    return {'name': 'Nema tog filma...'}

def vj02Filmovi(request):
    context = {'filmovi': getFilmovi()}
    return render(request, 'filmovi.html', context)

def vj02Film(request):

    context = {'film': getFilmById(randint(1, len(getFilmovi())))}
    return render(request, 'film.html', context)

def vj02FilmId(request, id):
    context = {'film': getFilmById(int(id))}
    return render(request, 'film.html', context)

def vj03(request):
    context = {'articles': Article.objects.filter(release_date__gte='2018-01-01')}
    return render(request, 'vj03.html', context)

@login_required
def vj04(request):
    if (request.method == "POST"):
        form = PasswordChangeForm(request.user, request.POST)
        pass
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'changePassword.html', {'form': form})
