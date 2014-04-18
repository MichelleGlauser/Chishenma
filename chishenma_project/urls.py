from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chishenma_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^chishenma_app/', include('chishenma_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^choose_food/$', 'chishenma_app.views.choose_food'),
	url(r'^help_me_decide/$', 'chishenma_app.views.help_me_decide'),
	url(r'^your_restaurants/$', 'chishenma_app.views.your_restaurants'),
	url(r'^restaurant_details/$', 'chishenma_app.views.restaurant_details'),
)
