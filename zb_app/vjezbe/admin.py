# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Author, Article, Knjiga
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','email')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'author')

@admin.register(Knjiga)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('naziv', 'autor')
