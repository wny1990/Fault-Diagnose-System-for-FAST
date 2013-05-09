from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, loader
import datetime

def homepage_view(request):

	return render(request,'homepage.html')
	
def test_view(request):
	now = datetime.datetime.now()
	context = Context({
               'now': now,
	})
	return render(request,'test.html',context)
def bttest_view(request):

	return render(request,'test1.html')
