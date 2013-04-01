from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, loader
from fault_data.models import FaultMode

def index(request):
	FaultMode_list = FaultMode.objects.order_by('FaultModeID')
	context = Context({
               'FaultMode_list': FaultMode_list,
	})
	return render(request,'modes/index.html',context)

def detail(request,mode_id):
	FaultMode_list = FaultMode.objects.order_by('FaultModeID')
	context = Context({
               'FaultModeID':mode_id,'FaultMode_list':FaultMode_list
	})

	return render(request,'details/details.html',context)

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
        msg = request.GET['search_text']
	FaultMode_list = FaultMode.objects.order_by('FaultModeID')
	context = Context({
               'FaultModeID':msg,'FaultMode_list':FaultMode_list
	})
	return render(request,'details/details.html',context)
