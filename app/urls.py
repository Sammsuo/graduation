from django.urls import path
from . import views

urlpatterns = {
    path('', views.index),
    path('logging', views.logging_in),
    path('logout', views.logging_out),
    path('register', views.register),

}