from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('h', views.say_hello),
    path('airport_list/', views.display, name='display')
]