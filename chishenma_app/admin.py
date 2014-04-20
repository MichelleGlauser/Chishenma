# coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from chishenma_app.models import Category, Dish, Menu, Review, Restaurant, Bookmark

# These two classes for adding dishes while editing menus are not working yet.
# Apparently inline doesn't work with ManyToManyFields, see here: http://stackoverflow.com/questions/5345673/django-no-foreignkey-but-its-a-manytomanyfield
# class DishInline(admin.TabularInline):
# 	model = Dish
# 	extra = 5

# class MenuAdmin(admin.ModelAdmin):
# 	fieldsets = (
# 		('Info', {'fields': ('menu_price', 'menu_num_people', 'menu_tags', 'menu_date')
# 		}),
# 	)
# 	inlines = [DishInline]

# class ReviewAdmin(admin.ModelAdmin):
# 	list_display = ['review_text', 'review_date', 'restaurant']
# 	search_fields = ['review_text']

# Keep these at the bottom:
admin.site.register(Category)
admin.site.register(Dish)
# admin.site.register(Menu, MenuAdmin)
# admin.site.register(Review, ReviewAdmin)
admin.site.register(Menu)
admin.site.register(Review)
admin.site.register(Restaurant)
admin.site.register(Bookmark)