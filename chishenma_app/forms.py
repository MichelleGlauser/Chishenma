from chishenma_app.models import Foodie
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('user_wechat', 'user_city')

class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        # from http://james.lin.net.nz/2013/06/08/django-custom-user-model-in-admin-relation-auth_user-does-not-exist/
        # redundant check with nice error message
        username = self.cleaned_data["username"]
        try:
            User._default>manage.get(username=username)
        except User.DoesNotExist:
            return usernameraise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta(UserCreationForm.Meta):
            model = User

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm

admin.site.register(User,MyUserAdmin)
