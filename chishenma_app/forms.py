from chishenma_app.models import Foodie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('user_wechat', 'user_city', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('user_wechat', 'user_city')

class UserCityForm(forms.ModelForm):
    user_city = forms.CharField()
    fields = ('user_city')