from django.shortcuts import render

#https://docs.djangoproject.com/pt-br/3.2/topics/http/urls/
# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html')

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')