"""levit_bell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from .views import *
from tips.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', inicio, name='inicio'),
    url(r'^politicas_privacidad/$', politicas_privacidad, name='politicas_privacidad'),
    url(r'^politica_empresarial/$', politica_empresarial, name='politica_empresarial'),
    url(r'^tips/$', mas_tips, name="mas_tips"),
]
