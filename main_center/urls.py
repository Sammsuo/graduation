from django.urls import path
from . import views

urlpatterns = {
    path('getRequest/post/', views.public_post)
}