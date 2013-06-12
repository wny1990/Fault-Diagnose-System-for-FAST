from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, loader
import datetime

def homepage_view(request):

	return render(request,'homepage.html')
	
def about_site_view(request):

	return render(request,'about_site.html')
	
def test_view(request):

	return render(request,'test.html')
