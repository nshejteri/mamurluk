from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'date_site_app/index.html', {})


def user_login(request):
	pass


def register(request):
	pass
	
