from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, loader
import datetime

def homepage_view(request):
	now = datetime.datetime.now()
	context = Context({
               'now': now,
	})
	return render(request,'homepage.html',context)
	
#def image(request,image_file):
#    image_data = open("/home/wny/fd_sys/mysite/images/image_file", "rb").read()
#    return HttpResponse(image_data, mimetype="image/png")
