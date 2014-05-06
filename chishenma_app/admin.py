# coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm, AdminPasswordChangeForm)
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from chishenma_app.models import Category, Dish, Menu, Review, Restaurant, Bookmark, Foodie


from models import Foodie #you can use get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import forms

class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta(UserCreationForm.Meta):
        model = Foodie

class MyUserAdmin(UserAdmin):  
    add_form = MyUserCreationForm
    fieldsets = (
        (None, {'fields': ('user_city', 'password', 'user_waitlist_status',
        		'user_waitlist_num', 'user_num_referrals')}),
    )
    add_fieldsets = (
        (None, {
  
        }),
    )
    form = UserChangeForm
    add_form = MyUserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('user_wechat', 'user_city', 'user_waitlist_status', 'user_waitlist_num', 'user_num_referrals')
    list_filter = ()
    search_fields = ('user_wechat', 'user_city', 'user_waitlist_status', 'user_waitlist_num', 'user_num_referrals')
    ordering = ('user_wechat',)
    filter_horizontal = ()

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
admin.site.register(Foodie,MyUserAdmin)
admin.site.register(Category)
admin.site.register(Dish)
# admin.site.register(Menu, MenuAdmin)
# admin.site.register(Review, ReviewAdmin)
admin.site.register(Menu)
admin.site.register(Review)
admin.site.register(Restaurant)
admin.site.register(Bookmark)