"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import os
from dotenv import load_dotenv
from django.contrib import admin
from django.urls import path, include


load_dotenv()

environment = os.environ.get("DJANGO_ENV")

urlpatterns = [
    path('api/', include([
        path('', include('api.v1.urls')),    
        path('', include('api.v2.urls'))    
    ])),
]


if environment.lower() == "development":
    urlpatterns += path('admin/', admin.site.urls),