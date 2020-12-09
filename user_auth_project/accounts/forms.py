from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm

class UserRegisterForm(UserCreationForm):
  first_name = forms.CharField(max_length=30)
  last_name = forms.CharField(max_length=30)
  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class UpdateUserForm(UserChangeForm):
  password = None
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']


'''
class UpdatePasswordForm(PasswordChangeForm):
  
  class Meta:
    model = User
    fields = ['username', 'password']
'''