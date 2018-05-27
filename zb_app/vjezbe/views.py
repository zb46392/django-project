# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import randint
from models import Author, Article, Knjiga
from forms import BookForm
from django.contrib.auth.decorators import user_passes_test


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

def vj05(request):
    isSuperUser = request.user.is_superuser
    isStaff = request.user.is_staff
    context = {'knjige':Knjiga.objects.all(), 'isSuperUser': isSuperUser, 'isStaff': isStaff}
    return render(request, 'books05.html', context)

def dodajKnjigu05(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            knjiga = Knjiga.objects.create()
            knjiga.naziv = form.cleaned_data['naziv']
            knjiga.autor = form.cleaned_data['autor']

            knjiga.save()

        return vj05(request)

    else:
        form = BookForm()
        context = {'form' : form}
        return render(request, 'bookForm.html', context)

def prominiKnjigu05(request, id):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            knjiga = Knjiga.objects.get(pk=id)

            knjiga.naziv = form.cleaned_data['naziv']
            knjiga.autor = form.cleaned_data['autor']

            knjiga.save()

        return vj05(request)

    else:
        knjiga = Knjiga.objects.get(pk=id)
        form = BookForm(initial={'naziv':knjiga.naziv, 'autor':knjiga.autor})

        context = {'form':form}
        return render(request, 'bookForm.html', context)


def vj06(request):
    isSuperUser = request.user.is_superuser
    isStaff = request.user.is_staff
    context = {'knjige':Knjiga.objects.all(), 'isSuperUser': isSuperUser, 'isStaff': isStaff}
    return render(request, 'books06.html', context)

def isSuperuser(user):
    return user.is_superuser

def isStaff(user):
    return user.is_staff


@user_passes_test(isSuperuser)
def dodajKnjigu06(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            knjiga = Knjiga.objects.create()
            knjiga.naziv = form.cleaned_data['naziv']
            knjiga.autor = form.cleaned_data['autor']

            knjiga.save()

        return vj06(request)

    else:
        form = BookForm()
        context = {'form' : form}
        return render(request, 'bookForm.html', context)

@user_passes_test(isStaff)
def prominiKnjigu06(request, id):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            knjiga = Knjiga.objects.get(pk=id)

            knjiga.naziv = form.cleaned_data['naziv']
            knjiga.autor = form.cleaned_data['autor']

            knjiga.save()

        return vj06(request)

    else:
        knjiga = Knjiga.objects.get(pk=id)
        form = BookForm(initial={'naziv':knjiga.naziv, 'autor':knjiga.autor})

        context = {'form':form}
        return render(request, 'bookForm.html', context)
