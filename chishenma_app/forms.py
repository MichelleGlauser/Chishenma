from chishenma_app.models import Foodie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth import forms
from django import forms

# class UserForm(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput())

# 	class Meta:
# 		model = User
# 		fields = ('user_wechat', 'user_city', 'password')

# class UserProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = UserProfile
# 		fields = ('user_wechat', 'user_city')

class UserCityForm(forms.Form):
    city = forms.CharField(max_length=25, required=True)
    fields = ('user_city,')

class WaitlistForm(forms.Form):
	email = forms.EmailField(max_length=35)
	fields = ('user_email,')
