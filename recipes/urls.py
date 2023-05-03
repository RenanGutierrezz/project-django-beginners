from django.urls import path
from recipes.views import home


#  eg: domain/sobre 
urlpatterns = [
    path('', home), # Home
]