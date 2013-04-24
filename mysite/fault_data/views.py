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
	search_list = FaultMode.objects.filter( FaultMode__contains = search_text) 
	context = Context({
               'search_list':search_list,
	})
	return render(request,'diagnose/search_list.html',context)

def manage_search(request):
	search_text = request.GET['search_text'] 
	search_list = FaultMode.objects.filter( FaultMode__contains = search_text) 
	context = Context({
               'search_list':search_list,
	})
	return render(request,'manage/search_list.html',context)

def diagnose(request):
	FaultMode_list = FaultMode.objects.order_by('FaultModeID')
	context = Context({
               'FaultMode_list': FaultMode_list,
	})
	return render(request,'diagnose/diagnose.html',context)
	
def datamanage(request):
	return render(request,'manage/data_manage.html')
	
def managelist(request):
	FaultMode_mlist = FaultMode.objects.order_by('FaultModeID')
	context = Context({
               'FaultMode_list': FaultMode_mlist,
	})
	return render(request,'manage/data_manage_list.html',context)
def dfunction(request,function_id):
	infile = open("/proc/meminfo")
	file_content = infile.read()
	test_result=file_content
	context = Context({
               'function_id': function_id,'test_result':test_result,
	})
	return render(request,'diagnose/dfunction.html',context)
	
def delmode(request,mode_id):
	action= "Delete"
#	FaultMode.objects.filter(FaultModeID = mode_id).delete()
	context = Context({
               'mode_id':mode_id,'action':action
	})
	return render(request,'manage/result.html',context)
	
def addmode(request):
	mode_id=1
	context = Context({
               'mode_id':mode_id,
	})
	return render(request,'manage/addmode.html',context)

def modifymode(request,mode_id):
	ChosenFaultMode = FaultMode.objects.filter(FaultModeID = mode_id)
	context = Context({
               'mode_id':mode_id,'ChosenFaultMode':ChosenFaultMode,
	})
	return render(request,'manage/modify.html',context)

def detailmodify(request,mode_id,attr):
	search_text = request.GET['search_text'] 
	if attr == 'FaultMode':
		FaultMode.objects.filter(FaultModeID = mode_id).update(FaultMode = search_text)
	if attr == 'FaultDescription':
		FaultMode.objects.filter(FaultModeID = mode_id).update(FaultDescription = search_text)
	if attr == 'HighLevelFaultModeID':
		FaultMode.objects.filter(FaultModeID = mode_id).update(HighLevelFaultModeID = search_text)
	if attr == 'DetectionMethod':
		FaultMode.objects.filter(FaultModeID = mode_id).update(DetectionMethod = search_text)
	if attr == 'ManualDetectionMethodID':
		FaultMode.objects.filter(FaultModeID = mode_id).update(ManualDetectionMethodID = search_text)
	if attr == 'FunctionID':
		FaultMode.objects.filter(FaultModeID = mode_id).update(FunctionID = search_text)
	if attr == 'Priority':
		FaultMode.objects.filter(FaultModeID = mode_id).update(Priority = search_text)
	if attr == 'LogicalRelationship':
		FaultMode.objects.filter(FaultModeID = mode_id).update(LogicalRelationship = search_text)
	context = Context({
               'mode_id':mode_id,'search_text':search_text,'attr':attr
	})
	return render(request,'manage/result.html',context)
