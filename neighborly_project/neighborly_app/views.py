from django.shortcuts import render, redirect
from django.template import RequestContext
from neighborly_app.CommercialRealestateScrape import get_listings
from neighborly_app.forms import PersonForm, SignUpForm
from neighborly_app.models import Person
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponse

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
	else:
		form = SignUpForm()
		return render(request, 'signup.html', {'form': form})

def index(request):
	return render(request,'index.html')

@login_required
def dataentry(request):
	if request.method == 'POST':
		form = PersonForm(request.POST, instance=request.user.person)
		
		if form.is_valid():
			form.save()
			return redirect('/currentresults/')
		else:
			form=PersonForm()
			return render(request,'dataentry.html',{'form': form})	
	else:
		form=PersonForm()
		return render(request,'dataentry.html',{'form': form})
	
@login_required
def currentresults(request):
	person = Person.objects.get(user=request.user)
	city=person.city
	state=person.state
	listings = get_listings(city,state)
	return render(request, 'currentresults.html',{'listings':listings})
	
