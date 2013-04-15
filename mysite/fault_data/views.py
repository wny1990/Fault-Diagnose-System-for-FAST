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
	ChosenFaultMode = FaultMode.objects.filter(FaultModeID = mode_id)
	list2 = FaultMode.objects.filter( HighLevelFaultModeID = mode_id) 
	context = Context({
               'FaultModeID':mode_id,'ChosenFaultMode':ChosenFaultMode,
	})

	return render(request,'details/details.html',context)

def dgdetail(request,mode_id):
	ChosenFaultMode = FaultMode.objects.filter(FaultModeID = mode_id)
	list2 = FaultMode.objects.filter( HighLevelFaultModeID = mode_id) 
	context = Context({
               'FaultModeID':mode_id,'ChosenFaultMode':ChosenFaultMode,'list2':list2
	})

	return render(request,'details/dgdetails.html',context)
	
def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	search_text = request.GET['search_text'] 
	
	return dgdetail(request,search_text)

def diagnose(request):
	FaultMode_list = FaultMode.objects.order_by('FaultModeID')
	context = Context({
               'FaultMode_list': FaultMode_list,
	})
	return render(request,'diagnose/diagnose.html',context)
