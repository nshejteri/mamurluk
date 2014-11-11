from django import forms
from django.contrib.auth.models import User
from date_site_app.models import UserProfile
from django.forms import CharField, BooleanField, Form, ChoiceField, DateField 
from models import UserProfile
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms.extras import widgets

class SignupForm(forms.Form):
	first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'autofocus': 'autofocus'}))
	last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'autofocus': 'autofocus'}))

	GENDER_CHOICES = ( 
     	('m', 'Male'), 
     	('f', 'Female'),
    )					 

	gender = ChoiceField(GENDER_CHOICES, label='Gender', required=True)
	#date_of_birth = forms.DateField(widget=SelectDateWidget(years=range(1950, datetime.date.today().year)))
	#date_of_birth = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"), input_formats=["%m/%d/%Y"])
	#date_of_birth = forms.DateField()
	#date_of_birth = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'myDateClass', 'placeholder':'Select a date'}))
	date_of_birth = forms.DateField(required=True, widget=SelectDateWidget(years=range(1950, datetime.date.today().year)))
	#birthday = forms.DateField(required=True)

	def signup(self, request, user):

		gender = self.cleaned_data['gender']
		date_of_birth = self.cleaned_data['date_of_birth']
		profile = UserProfile(user=user, gender=gender, date_of_birth=date_of_birth)
		profile.save()