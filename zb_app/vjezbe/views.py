# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import randint
from models import Author, Article, Knjiga
from forms import BookForm, BmiForm
from .bmi import bmi_calc, BmiManager
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import View
import requests
import json
from django.template.loader import render_to_string
from django.http import JsonResponse


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
    context = {'knjige':Knjiga.objects.all()}
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


def vj07(request):
    mozeMjenjat = request.user.has_perm('vjezbe.mozeMjenjat')
    mozeDodat = request.user.has_perm('vjezbe.mozeDodat')
    context = {'knjige':Knjiga.objects.all(), 'mozeMjenjat': mozeMjenjat, 'mozeDodat': mozeDodat}
    return render(request, 'books07.html', context)

def dodajKnjigu07(request):
    if request.user.has_perm('vjezbe.mozeDodat'):
        if request.method == 'POST':
            form = BookForm(request.POST)

            if form.is_valid():
                knjiga = Knjiga.objects.create()
                knjiga.naziv = form.cleaned_data['naziv']
                knjiga.autor = form.cleaned_data['autor']

                knjiga.save()

            return vj07(request)

        else:
            form = BookForm()
            context = {'form' : form}
            return render(request, 'bookForm.html', context)

    return vj07(request)


def prominiKnjigu07(request, id):
    if request.user.has_perm('vjezbe.mozeMjenjat'):
        if request.method == 'POST':
            form = BookForm(request.POST)

            if form.is_valid():
                knjiga = Knjiga.objects.get(pk=id)

                knjiga.naziv = form.cleaned_data['naziv']
                knjiga.autor = form.cleaned_data['autor']

                knjiga.save()

            return vj07(request)

        else:
            knjiga = Knjiga.objects.get(pk=id)
            form = BookForm(initial={'naziv':knjiga.naziv, 'autor':knjiga.autor})

            context = {'form':form}
            return render(request, 'bookForm.html', context)

    return vj07(request)


def bmi(request):
	if request.method == 'GET':
		form = BmiForm()
	elif request.method == 'POST':
		form = BmiForm(request.POST)
		if form.is_valid(): # ukliko je forma validna napraviti cem se izracun
			weigth = form.cleaned_data.get('weigth')
			heigth = form.cleaned_data.get('heigth')

			bmi_manager = BmiManager(weigth, heigth)
			bm_index =  bmi_manager.calculate()

			return render(request, 'success.html', {'bmi': bm_index})


	return render(request, 'bmi.html',{'form': form})



class vj09view01(View):
    def get(self, request):
        r = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22split%2C%20hr%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
        if r.status_code == 200:
            weather_object = json.loads(r.content)
            return render(request, 'weather.html',{'data': weather_object['query']['results']['channel']})
            #return render_to_string('weather.html', {'data': weather_object['query']['results']['channel']['item']['description']})
            #return JsonResponse({'data': weather_object})
        else:
            return HttpResponse("No service!!!Try later!!!")


class vj09view02(View):
    template_name = 'weather02.html'
    def get(self, request):
        return render(request, 'weather02.html')
    def post(self, request):
        r = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22split%2C%20hr%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
        data = None
        if r.status_code == 200:
            weather_object = json.loads(r.content)
            data = {
            'imageUrl': weather_object['query']['results']['channel']['image']['url'],
            'title': weather_object['query']['results']['channel']['item']['title'],
            'forecast': weather_object['query']['results']['channel']['item']['forecast']
            }
        else:
            data = {'msg': 'No service!!!Try later!!!'}

        return JsonResponse({'yapi': data})


class Ajax(View):
    template_name = 'ajax.html'

    def get(self, request):
        template = render_to_string(self.template_name)
        return JsonResponse({'template': template})
