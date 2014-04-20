# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.views.generic import TemplateView

from chishenma_app.models import Category, Dish, Menu, Review, Restaurant, Bookmark, User


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context

def index(request):
	if not request.user.is_authenticated():
		form = AuthenticationForm(request)
	else:
		form = None
	context = {'form':form}
	populateContext(request, context)
	return render(request, 'chishenma/index.html', context)

def login(request):
	context = {}
	try:
		username = request.GET['username']
		password = request.GET['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
			else:
				context['error'] = 'Non active user'
		else:
			context['error'] = 'Wrong username or password'
	except:
		context['error'] = ''

    	populateContext(request, context)
    	return render(request, 'chishenma/index.html', context)

def logout(request):
	context = {}
	try:
		auth_logout(request)
	except:
		context['error'] = 'Some error occured.'

	populateContext(request, context)
	return render(request, 'index.html', context)

def populateContext(request, context):
	context['authenticated'] = request.user.is_authenticated()
	if context['authenticated'] == True:
		context['username'] = request.user.username


def auth_view(request):
	# wechat = request.POST.get('wechat_id', '')
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = authenticate(username=username, password=password)
	# user = auth.authenticate(wechat_id=wechat_id, password=password)

	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('chishenma/loggedin/')
	else:
		return HttpResponseRedirect('chishenma/invalid_login/')

	# if user is not None:
	# auth.login(request, user)
	# return HttpResponseRedirect('chishenma/loggedin/')
	# else:
	# return HttpResponseRedirect('chishenma/invalid_login/')

def loggedin(request):
	return render(request, 'chishenma/loggedin.html',
	{'full_name': request.user.username})

def invalid_login(request):
	return render(request, 'chishenma/invalid_login.html')

def logout(request):
	auth.logout(requets)
	return render(request, 'chishenma/logout.html')





def choose_food(request):
	return HttpResponse("Choose your food here.")

def help_me_decide(request):
	return render(request, 'chishenma/help_me_decide.html')

def your_restaurants(request):
	return render(request, 'chishenma/your_restaurants.html')

# Can change to "(request, rest_name_en)" for specific URLs
def restaurant_details(request):
	# Add "% rest_name_en" at the end to have that as part of the URL:
	return HttpResponse("Here are the deets.") 