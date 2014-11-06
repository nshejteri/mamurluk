from django import forms
from django.contrib.auth.models import User
from date_site_app.models import UserProfile
from django.forms import CharField, BooleanField, Form, ChoiceField, DateField 
from models import UserProfile

class SignupForm(forms.Form):
	first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'autofocus': 'autofocus'}))
	last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'autofocus': 'autofocus'}))

	GENDER_CHOICES = ( 
     	('m', 'Male'), 
     	('f', 'Female'),
    )					 

	gender = ChoiceField(GENDER_CHOICES, label='Gender', required=True) 

	class Meta: 
         model = UserProfile 

	def signup(self, request, user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.gender = self.cleaned_data['gender']
		user.save()