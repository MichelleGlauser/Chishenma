# coding=utf-8
from __future__ import unicode_literals
# from django.http import Http404 Need to make a 404.html, raise on notexist
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.transaction import atomic
from django.template import RequestContext, loader
from django.views.generic import TemplateView
from chishenma_app.forms import UserWaitlistForm
from chishenma_app.models import Foodie
# from django.contrib.auth.models import User, Permission
# from bouncer.functions import add_to_waitlist

from chishenma_app.models import Category, Dish, Menu, Review, Restaurant, Bookmark, User


def index(request):
	user_form = UserCreationForm()
	user_waitlist_form = UserWaitlistForm()

	if request.method == 'POST':
		user_form = UserCreationForm(request.POST)
		user_waitlist_form = UserWaitlistForm(request.POST)

	if user_form.is_valid() and user_waitlist_form.is_valid():
		new_user = user_form.save()
		Foodie.objects.create(user_wechat=new_user, user_email=user_waitlist_form['user_email'].value(), user_city=user_waitlist_form['user_city'].value())

		# return redirect(reverse('home'))
		return render(request, 'registration/waiting_list.html)

	return render(request, 'chishenma/index.html', {
		'user_form': user_form,
		'user_waitlist_form': user_waitlist_form,
	})
	# if not request.user.is_authenticated():
	# 	form = AuthenticationForm(request)
	# else:
	# 	form = None
	# context = {'form':form}
	# return render(request, 'chishenma/index.html', context)

@atomic
def register(request):
	user_form = UserCreationForm()
	user_waitlist_form = UserWaitlistForm()

	if request.method == 'POST':
		user_form = UserCreationForm(request.POST)
		user_waitlist_form = UserWaitlistForm(request.POST)

	if user_form.is_valid() and user_waitlist_form.is_valid():
		new_user = user_form.save()
		Foodie.objects.create(user_wechat=new_user, user_email=user_waitlist_form['user_email'].value(), user_city=user_waitlist_form['user_city'].value())

		return redirect(reverse('home'))

	return render(request, 'registration/register.html', {
		'user_form': user_form,
		'user_waitlist_form': user_waitlist_form,
	})

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

	return render(request, 'chishenma/index.html', context)

def logout(request):
	context = {}
	try:
		auth_logout(request)
	except:
		context['error'] = 'Some error occured.'

	return render(request, 'chishenma/index.html', context)

def auth_view(request):
	# wechat = request.POST.get('wechat_id', '')
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = authenticate(username=username, password=password)

	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('registration/loggedin/')
	else:
		return HttpResponseRedirect('registration/invalid_login/')

def loggedin(request):
	return render(request, 'registration/loggedin.html',
	{'full_name': request.user.username})

def invalid_login(request):
	return render(request, 'registration/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'registration/logout.html')

def waiting_list(request):
	return render(request, 'registration/waiting_list.html')



def choose_category(request):
	# , category_label, category_img, category_tag
	# category_list = Category.objects.filter(category=category_id)
	# for c in category_list:

	return render(request, 'chishenma/choose_category.html')

def help_me_decide(request):
	# take results of sorting, do something
	return render(request, 'chishenma/help_me_decide.html')

def your_restaurants(request):
	context = {}
	return render(request, 'chishenma/your_restaurants.html', context)
	# return render_to_response('chishenma/your_restaurants.html',
	# 						 {'restaurants': Restaurant.objects.all() })
# def your_restaurants(request, rest_id):
	# rests = Restaurant.objects.filter(rest_id=rest_id)
	# return render(request, 'chishenma/your_restaurants.html', {'rests':rests})
	# return HttpResponse("These restaurants may interest you.")

# Can change to "(request, rest_name_en)" for specific URLs
def restaurant_details(request, rest_id=1):
	context = {}
	# Add "% rest_name_en" at the end to have that as part of the URL:
	# return HttpResponse("Here are the deets for restaurant %s!" % rest_id) 
	return render(request, 'chishenma/restaurant_details.html', context)
	# return render_to_response('chishenma/restaurant_details.html',
	# 						 {'restaurant': Restaurant.objects.get(id=rest_id) })