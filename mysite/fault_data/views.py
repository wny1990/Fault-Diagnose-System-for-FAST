from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, loader
from fault_data.models import FaultMode

def databrose(request):
	FaultMode_list = FaultMode.objects.order_by('FaultModeID')
	context = Context({
               'FaultMode_list': FaultMode_list,
	})
	return render(request,'modes/databrose.html',context)

def detail(request,mode_id):
	FaultMode_list = FaultMode.objects.order_by('FaultModeID')
	list2 = FaultMode.objects.filter( HighLevelFaultModeID=mode_id) 
	context = Context({
               'FaultModeID':mode_id,'FaultMode_list':FaultMode_list,'list2':list2
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

def diagnose(request):
	FaultMode_list = FaultMode.objects.order_by('FaultModeID')
	context = Context({
               'FaultMode_list': FaultMode_list,
	})
	return render(request,'diagnose/diagnose.html',context)
