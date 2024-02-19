from django.urls import path

from menu.apps import MenuConfig
from menu.views import index

app_name = MenuConfig.name

urlpatterns = [
    path('', index, name='index')
]
