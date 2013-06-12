from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, loader
from fault_data.models import *

def data_browse(request):
	list0 = FaultModeRelation.objects.filter( HighLevelFaultModeID = 0)
	list1=list0.values_list('FaultModeID')
	list2 = FaultMode.objects.filter(FaultModeID__in= list1) 
	context = Context({
               'HighLevelFaultMode_list': list2,
	})
	return render(request,'modes/databrowse.html',context)
	
def browse_all_mode(request):
	FaultMode_list = FaultMode.objects.order_by('FaultModeID')
	context = Context({
               'FaultMode_list': FaultMode_list,
	})
	return render(request,'modes/browseall.html',context)
	
def browse_all_cause(request):
	FaultCause_list = FaultCause.objects.order_by('FaultCauseID')
	context = Context({
               'FaultCause_list': FaultCause_list,
	})
	return render(request,'modes/browseall.html',context)
	
def mode_detail(request,mode_id):
	ChosenFaultMode = FaultMode.objects.filter(FaultModeID = mode_id)
	list0 = FaultModeRelation.objects.filter( HighLevelFaultModeID = mode_id)
	list1=list0.values_list('FaultModeID')
	list2 = FaultMode.objects.filter(FaultModeID__in= list1) 
	context = Context({
               'FaultModeID':mode_id,'ChosenFaultMode':ChosenFaultMode,'list2':list2
	})

	return render(request,'details/mode_details.html',context)
	
def cause_detail(request,cause_id):
	ChosenFaultCause = FaultCause.objects.filter(FaultCauseID = cause_id)
	context = Context({
               'FaultCauseID':cause_id,'ChosenFaultCause':ChosenFaultCause,
	})

	return render(request,'details/cause_details.html',context)
	
def dgdetail(request,mode_id):
	ChosenFaultMode = FaultMode.objects.filter(FaultModeID = mode_id)
#	list2 = FaultMode.objects.filter( HighLevelFaultModeID = mode_id)
	list0 = FaultModeRelation.objects.filter( HighLevelFaultModeID = mode_id)
	list1=list0.values_list('FaultModeID')
	SonFaultMode = FaultMode.objects.filter(FaultModeID__in= list1)
	
	list0 = FaultCauseRelation.objects.filter( FaultModeID = mode_id)
	list1 = list0.values_list('FaultCauseID')
	SonFaultCause = FaultCause.objects.filter(FaultCauseID__in= list1) 
	
	context = Context({
               'FaultModeID':mode_id,'ChosenFaultMode':ChosenFaultMode,'SonFaultMode':SonFaultMode,'SonFaultCause':SonFaultCause,
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
	FaultMode_list= FaultMode.objects.all()
	list0 = FaultModeRelation.objects.filter( HighLevelFaultModeID = 0)
	list1=list0.values_list('FaultModeID')
	list2 = FaultMode.objects.filter(FaultModeID__in= list1) 
	
	context = Context({
               'HighLevelFaultMode_list': list2, 'FaultMode_list': FaultMode_list,
	})
	return render(request,'diagnose/diagnose.html',context)
	
def datamanage(request):
	return render(request,'manage/data_manage.html')
	
def syslog(request):
	return render(request,'syslog/syslog_main.html')
	
def manage_mode_list(request):
	FaultMode_Manage_list = FaultMode.objects.order_by('FaultModeID')
	context = Context({
               'FaultMode_list': FaultMode_Manage_list,
	})
	return render(request,'manage/manage_mode_list.html',context)
	
def manage_cause_list(request):
	FaultCause_Manage_list = FaultCause.objects.order_by('FaultCauseID')
	context = Context({
               'FaultCause_list': FaultCause_Manage_list,
	})
	return render(request,'manage/manage_cause_list.html',context)

def manage_relation_list(request):
	ModeMode_Relation_list = FaultModeRelation.objects.order_by('FaultModeID')
	ModeCause_Relation_list= FaultCauseRelation.objects.order_by('FaultModeID')
	context = Context({
               'ModeMode_Relation_list':ModeMode_Relation_list,'ModeCause_Relation_list':ModeCause_Relation_list,
	})
	return render(request,'manage/manage_relation_list.html',context)
	

	
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
	
def add_mode_data(request):
	return render(request,'manage/add_mode_data.html')
	
def add_cause_data(request):
	mode_id=1
	context = Context({
               'mode_id':mode_id,
	})
	return render(request,'manage/add_mode_data.html',context)

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
#	if attr == 'HighLevelFaultModeID':
#		FaultMode.objects.filter(FaultModeID = mode_id).update(HighLevelFaultModeID = search_text)
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
               'mode_id':mode_id,'modify_text':search_text,'attr':attr
	})
	return render(request,'manage/result.html',context)


def addmodeattr(request):
	FaultModeID = request.GET['FaultModeID'] 
	FaultMode = request.GET['FaultMode'] 
	FaultDescription = request.GET['FaultDescription']
#	HighLevelFaultModeID = request.GET['HighLevelFaultModeID']
	DetectionMethod = request.GET['DetectionMethod'] 
	ManualDetectionMethodID = request.GET['ManualDetectionMethodID'] 
	FunctionID = request.GET['FunctionID'] 
	Priority = request.GET['Priority'] 
	FaultDescription = request.GET['LogicalRelationship'] 
	addattr=1
#	context = Context({
#               'addattr':addattr,'FaultModeID':FaultModeID,'FaultMode':FaultMode,'FaultDescription':FaultDescription,'HighLevelFaultModeID':HighLevelFaultModeID,
#	})
	context = Context({
               'addattr':addattr,'FaultModeID':FaultModeID,'FaultMode':FaultMode,'FaultDescription':FaultDescription,
	})
	return render(request,'manage/result.html',context)
