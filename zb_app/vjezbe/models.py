# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 40, null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 40)
    release_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Knjiga(models.Model):
    naziv = models.CharField(max_length = 40)
    autor = models.CharField(max_length = 40)

    class Meta:
        permissions = (
            ("mozeMjenjat", "moze mjenjat podatke o knjizi"),
            ("mozeDodat", "moze dodatvati knjige"), )
