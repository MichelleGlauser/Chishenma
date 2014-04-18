from django.shortcuts import render
from django.http import HttpResponse
# from django.template import RequestContext, loader

from chishenma_app.models import Category, Dish, Menu, Review, Restaurant, Bookmark

def index(request):
	return render(request, 'chishenma/index.html')

def choose_food(request):
	return HttpResponse("Choose your food here.")

def help_me_decide(request):
	return render(request, 'chishenma/help_me_decide.html')

def your_restaurants(request):
	return HttpResponse("It sounds like one of these places might suit your fancy.")

# Can change to "(request, rest_name_en)" for specific URLs
def restaurant_details(request): 
# Add "% rest_name_en" at the end to have that as part of the URL:
	return HttpResponse("Here are the deets.") 