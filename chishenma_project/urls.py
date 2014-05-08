# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from chishenma_app.models import Category, Dish, Menu, Review, Restaurant, Bookmark, User
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'chishenma_app.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^/$', TemplateView.as_view(template_name='index.html'), name='home'),
    # url(r'^$', 'chishenma_app.views.index'),

    # user auth urls
    url(r'^auth/$', 'chishenma_app.views.auth_view'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^loggedin/$', 'chishenma_app.views.loggedin'),
    url(r'^invalid/$', 'chishenma_app.views.invalid_login'),
    url(r'^register/$', 'chishenma_app.views.register'),
    # url(r'^waitinglist/', include('waitinglist.urls')),

    # page urls
    url(r'^choose_category/$', 'chishenma_app.views.choose_category', name="choose_category"),
    url(r'^help_me_decide/$', 'chishenma_app.views.help_me_decide', name="help_me_decide"),
    url(r'^your_restaurants/$', 'chishenma_app.views.your_restaurants', name="your_restaurants"),
    url(r'^restaurant_details/$', 'chishenma_app.views.restaurant_details', name="restaurant_details"),
    # url(r'^restaurant_details/(?P<rest_id>\d+)/$', 'chishenma_app.views.restaurant_details', name="restaurant_details"),
)