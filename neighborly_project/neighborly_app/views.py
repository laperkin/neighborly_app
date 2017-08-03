from django.shortcuts import render_to_response, render
from django.template import RequestContext
from neighborly_app.CommercialRealestateScrape import get_listings
from neighborly_app.forms import UserForm

def index(request):
	if request.method=='POST':
		return render(request, 'currentresults.html')
	else:
		form = UserForm()
		return render(request,'index.html',context={'form':form},)

def currentresults(request):
	listings = get_listings('Raleigh','NC')
	return render(request,'currentresults.html',context={'list':listings})
