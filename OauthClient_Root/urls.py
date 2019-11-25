# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from .views import login_oauth, callback, saldo
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^saldo/', saldo, name='saldo'),
    url(r'^login/', login_oauth, name='login'),
    url(r'^callback/', callback, name='callback'),

    url(r'^admin/', admin.site.urls),
]
