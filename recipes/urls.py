from django.urls import path

from . import views

# recipes:recipe
app_name = 'recipes'


#  eg: domain/sobre 
urlpatterns = [
    path('', views.home, name="home"), # Home
    path('recipes/<int:id>/',views.recipe, name="recipe"), 
]