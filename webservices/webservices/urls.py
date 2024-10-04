"""
URL configuration for webservices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from dog.viewsets import DogViewSet, BreedViewSet

#This handles the creation of routes for viewsets based on the methods avaliable.
router = DefaultRouter()
#Using this creates a base url prefix /dogs/
router.register(r'dogs', DogViewSet, basename='dog')
#Using this creates a base url prefix /breads/
router.register(r'breeds', BreedViewSet, basename='breed')

urlpatterns = [
    path('admin/', admin.site.urls),
    #THis will include all the router urls created earlier
    path('', include(router.urls)),
]

