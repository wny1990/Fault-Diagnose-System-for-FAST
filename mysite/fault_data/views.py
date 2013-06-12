from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, loader
from fault_data.models import *

def add_mode_attr(request):
	FaultModeID = request.GET['FaultModeID'] 
	FaultMode = request.GET['FaultMode'] 
	FaultDescription = request.GET['FaultDescription']
	DetectionMethod = request.GET['DetectionMethod'] 
	ManualDetectionMethodID = request.GET['ManualDetectionMethodID'] 
	FunctionID = request.GET['FunctionID'] 
	Priority = request.GET['Priority'] 
	LogicalRelationship = request.GET['LogicalRelationship'] 
	addattr=1
	p=FaultMode(FaultModeID= aFaultModeID,FaultMode= aFaultmode,FaultDescription= aFaultDescription ,DetectionMethod=aDetectionMethod,ManualDetectionMethodID=aManualDetectionMethodID,FunctionID=aFunctionID,Priority=aPriority,LogicalRelationship=aLogicalRelationship)
	p.save()
	context = Context({
			   'addattr':addattr,'FaultModeID':aFaultModeID,'FaultMode':aFaultMode,'FaultDescription':aFaultDescription,'DetectionMethod':aDetectionMethod,'ManualDetectionMethodID':aManualDetectionMethodID,'FunctionID':aFunctionID,'Priority':aPriority,'LogicalRelationship':aLogicalRelationship,
	})
	return render(request,'manage/mode_result.html',context)
	
def add_cause_attr(request):
	aFaultCauseID = request.GET['FaultCauseID'] 
	aFaultCause = request.GET['FaultCause'] 
	aFaultCauseDescription = request.GET['FaultCauseDescription']
	aDetectionMethod = request.GET['DetectionMethod'] 
	aManualDetectionMethodID = request.GET['ManualDetectionMethodID'] 
	aFunctionID = request.GET['FunctionID'] 
	aPriority = request.GET['Priority'] 
	aLogicalRelationship = request.GET['LogicalRelationship'] 
	aMaintenanceSuggestions=request.GET['MaintenanceSuggestions']
	addattr=1
	p=FaultCause(FaultCauseID= aFaultCauseID,FaultCause= aFaultCause,FaultCauseDescription= aFaultCauseDescription ,DetectionMethod=aDetectionMethod,ManualDetectionMethodID=aManualDetectionMethodID,FunctionID=aFunctionID,Priority=aPriority,LogicalRelationship=aLogicalRelationship,MaintenanceSuggestions=aMaintenanceSuggestions)
	p.save()
	context = Context({
			   'addattr':addattr,'FaultCauseID':aFaultCauseID,'FaultCause':aFaultCause,'FaultCauseDescription':aFaultCauseDescription,'DetectionMethod':aDetectionMethod,'ManualDetectionMethodID':aManualDetectionMethodID,'FunctionID':aFunctionID,'Priority':aPriority,'LogicalRelationship':aLogicalRelationship,'MaintenanceSuggestions':aMaintenanceSuggestions,
	})
	return render(request,'manage/cause_result.html',context)

def add_mode_data(request):
	return render(request,'manage/add_mode_data.html')
	
def add_cause_data(request):
	return render(request,'manage/add_cause_data.html')
	
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
	
	
def cause_detail(request,cause_id):
	ChosenFaultCause = FaultCause.objects.filter(FaultCauseID = cause_id)
	context = Context({
               'FaultCauseID':cause_id,'ChosenFaultCause':ChosenFaultCause,
	})

	return render(request,'details/cause_details.html',context)
	
def dgdetail(request,mode_id):
	ChosenFaultMode = FaultMode.objects.filter(FaultModeID = mode_id)
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

def cause_manage_search(request):
	search_text = request.GET['search_text'] 
	search_list = FaultCause.objects.filter( FaultCause__contains = search_text) 
	context = Context({
               'search_list':search_list,
	})
	return render(request,'manage/cause_search_list.html',context)
	

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
	FaultMode.objects.filter(FaultModeID = mode_id).delete()
	context = Context({
               'mode_id':mode_id,'action':action
	})
	return render(request,'manage/mode_result.html',context)

def delcause(request,cause_id):
	action= "Delete"
	FaultCause.objects.filter(FaultCauseID = cause_id).delete()
	context = Context({
               'cause_id':cause_id,'action':action
	})
	return render(request,'manage/cause_result.html',context)
	
def del_mm_relation(request,mode_id1,mode_id2):
	action= "Delete"
	FaultModeRelation.objects.filter(HighLevelFaultModeID = mode_id2 , FaultModeID = mode_id1).delete()
	context = Context({
               'mode_id1':mode_id1,'action':action,'mode_id2':mode_id2,
	})
	return render(request,'manage/mm_relation_result.html',context)

def del_mc_relation(request,mode_id,cause_id):
	action= "Delete"
	FaultCauseRelation.objects.filter(FaultCauseID = cause_id, FaultModeID = mode_id).delete()
	context = Context({
               'mode_id':mode_id,'cause_id':cause_id,'action':action,
	})
	return render(request,'manage/mc_relation_result.html',context)
	
def mode_detailmodify(request,mode_id,attr):
	search_text = request.GET['search_text'] 
	if attr == 'FaultMode':
		FaultMode.objects.filter(FaultModeID = mode_id).update(FaultMode = search_text)
	if attr == 'FaultDescription':
		FaultMode.objects.filter(FaultModeID = mode_id).update(FaultDescription = search_text)
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
	return render(request,'manage/mode_result.html',context)	
	
def cause_detailmodify(request,cause_id,attr):
	search_text = request.GET['search_text'] 
	if attr == 'FaultCause':
		FaultCause.objects.filter(FaultCauseID = cause_id).update(FaultCause = search_text)
	if attr == 'FaultCauseDescription':
		FaultCause.objects.filter(FaultCauseID = cause_id).update(FaultCauseDescription = search_text)
	if attr == 'DetectionMethod':
		FaultCause.objects.filter(FaultCauseID = cause_id).update(DetectionMethod = search_text)
	if attr == 'ManualDetectionMethodID':
		FaultCause.objects.filter(FaultCauseID = cause_id).update(ManualDetectionMethodID = search_text)
	if attr == 'FunctionID':
		FaultCause.objects.filter(FaultCauseID = cause_id).update(FunctionID = search_text)
	if attr == 'Priority':
		FaultCause.objects.filter(FaultCauseID = cause_id).update(Priority = search_text)
	if attr == 'LogicalRelationship':
		FaultCause.objects.filter(FaultCauseID = cause_id).update(LogicalRelationship = search_text)
	if attr == 'MaintenanceSuggestions':
		FaultCause.objects.filter(FaultCauseID = cause_id).update(MaintenanceSuggestions = search_text)
	context = Context({
               'cause_id':cause_id,'modify_text':search_text,'attr':attr
	})
	return render(request,'manage/cause_result.html',context)	
	
def modifymode(request,mode_id):
	ChosenFaultMode = FaultMode.objects.filter(FaultModeID = mode_id)
	context = Context({
               'mode_id':mode_id,'ChosenFaultMode':ChosenFaultMode,
	})
	return render(request,'manage/mode_modify.html',context)

def modifycause(request,cause_id):
	ChosenFaultCause = FaultCause.objects.filter(FaultCauseID = cause_id)
	context = Context({
               'cause_id':cause_id,'ChosenFaultCause':ChosenFaultCause,
	})
	return render(request,'manage/cause_modify.html',context)
	

def mode_detail(request,mode_id):
	ChosenFaultMode = FaultMode.objects.filter(FaultModeID = mode_id)
	list0 = FaultModeRelation.objects.filter( HighLevelFaultModeID = mode_id)
	list1=list0.values_list('FaultModeID')
	list2 = FaultMode.objects.filter(FaultModeID__in= list1) 
	context = Context({
               'FaultModeID':mode_id,'ChosenFaultMode':ChosenFaultMode,'list2':list2
	})

	return render(request,'details/mode_details.html',context)
	
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

def mode_manage_search(request):
	search_text = request.GET['search_text'] 
	search_list = FaultMode.objects.filter( FaultMode__contains = search_text) 
	context = Context({
               'search_list':search_list,
	})
	return render(request,'manage/mode_search_list.html',context)
		
def syslog(request):
	return render(request,'syslog/syslog_main.html')

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	search_text = request.GET['search_text'] 
	search_list = FaultMode.objects.filter( FaultMode__contains = search_text) 
	context = Context({
               'search_list':search_list,
	})
	return render(request,'diagnose/search_list.html',context)
