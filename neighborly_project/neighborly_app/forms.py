from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from neighborly_app.models import Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['email','city','state','zip_code']
		
class SignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
	