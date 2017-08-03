from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from neighborly_app.CommercialRealestateScrape import get_listings
from neighborly_app.forms import PersonForm, SignUpForm
from neighborly_app.models import Person
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
		return render(request, 'signup.html', {'form': form})

def index(request):
	return render(request,'index.html')

def dataentry(request):
	if request.method == 'POST':
		form = PersonForm(data=reqeust.POST)
		if form.is_valid():
			form.save()
			return redirect('/currentresults/')
	else:
		form=PersonForm()
		return render(request,'dataentry.html',{'form': form})
	

def currentresults(request):
	Person.objects.get(user=request.user)
	
	return render(request, 'dataentry.html')
	
