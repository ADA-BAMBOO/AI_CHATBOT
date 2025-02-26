from django.contrib import admin
from django.urls import path,include
from .views import GetJsonAPI
urlpatterns = [
    path('', GetJsonAPI.as_view(),name='answering'),
]
