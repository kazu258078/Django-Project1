from django.urls import path

from .views import hellofunction


urlpatterns = [
    #hello/worldと書いてはいけない
    path('world/', hellofunction), 
]
