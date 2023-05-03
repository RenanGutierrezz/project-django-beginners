from django.urls import path
from recipes.views import home, contato, sobre


#  eg: domain/sobre 
urlpatterns = [
    path('', home), # Home
    path('contato/', contato), # /contato/
    path('sobre/', sobre), # /sobre/
]