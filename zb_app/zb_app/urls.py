"""zb_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView)
from vjezbe import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vj01/$', views.vj01),
    url(r'^filmovi/$', views.vj02Filmovi),
    url(r'^film/([0-9]+)/$', views.vj02FilmId),
    url(r'^film/$', views.vj02Film),
    url(r'^vj03/$', views.vj03),
    url(r'^login/$', LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$',LogoutView.as_view(next_page='chpass'), name='logout'),
    url(r'^vj04/$', PasswordChangeView.as_view(
        template_name="changePassword.html",
        success_url='passwordChangeDone'), name='chpass'),
    url(r'^vj04/passwordChangeDone/$', PasswordChangeDoneView.as_view(
        template_name="changePasswordDone.html"), name='chpassdone'),
    url(r'^vj05/$', views.vj05),
    url(r'^book05/$', views.dodajKnjigu05, name='bookForm05'),
    url(r'^book05/([0-9]+)$', views.prominiKnjigu05, name='chBookForm05'),
    url(r'^vj06/$', views.vj06),
    url(r'^book06/$', views.dodajKnjigu06, name='bookForm06'),
    url(r'^book06/([0-9]+)$', views.prominiKnjigu06, name='chBookForm06'),
    url(r'^vj07/$', views.vj07),
    url(r'^book07/$', views.dodajKnjigu07, name='bookForm07'),
    url(r'^book07/([0-9]+)$', views.prominiKnjigu07, name='chBookForm07'),
    url(r'^vj08/$', views.bmi, name='bmi'),

]
