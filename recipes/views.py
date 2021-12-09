from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.views import generic


def recipes(request):
    return HttpResponse(request,'meals.html')















 

#class RecipeListView(generic.ListView):
    template_name = r'C:\Users\blair\Documents\GitHub\Recipe_Manager-Calender\recipes\templates'
    context_object_name = 'r'
    
    def get_queryset(self):
        return Recipe.objects.all()
    



#def index(request):
    #recipes = Recipe.objects.all()
    #return render(request,' recipes/recipes.html', {'recipes': recipes})

    

# Create your views here.
