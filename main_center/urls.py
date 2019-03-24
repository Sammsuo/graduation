from django.urls import path
from . import views

urlpatterns = {
    path('getRequest/post/', views.choose_method),
    path('APItest/test', views.testUp),
    path('APItest/runTest', views.run_api_test)
}