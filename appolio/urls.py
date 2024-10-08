"""
URL configuration for appolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from investo import urls as investo_urls
from rentoro import urls as rentoro_urls
from appolio.api import api
import datetime


def get_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    html = f"<html><body>IP: {ip}</body></html>"
    return HttpResponse(html)


urlpatterns = [
    path('rentoro/', include(rentoro_urls)),
    path('investo/', include(investo_urls)),
    path('api/', api.urls),
    path('', get_ip)
]
