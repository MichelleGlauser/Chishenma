# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'chishenma_app.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^chishenma_app/', include('chishenma_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^/$', TemplateView.as_view(template_name='index.html'), name='home'),
    # url(r'^$', 'chishenma_app.views.index'),

    # user auth urls
    url(r'^auth/$', 'chishenma_app.views.auth_view'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^loggedin/$', 'chishenma_app.views.loggedin'),
    url(r'^invalid/$', 'chishenma_app.views.invalid_login'),

    # page urls
    url(r'^choose_category/$', 'chishenma_app.views.choose_category'),
    url(r'^help_me_decide/$', 'chishenma_app.views.help_me_decide'),
    url(r'^your_restaurants/$', 'chishenma_app.views.your_restaurants'),
    url(r'^restaurant_details/$', 'chishenma_app.views.restaurant_details'),
)