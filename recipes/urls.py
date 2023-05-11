from django.urls import path

from . import views


#  eg: domain/sobre 
urlpatterns = [
    path('', views.home), # Home
    path('recipes/<int:id>/',views.recipe), 
]