
from django.conf.urls import patterns, url

from fault_data import views

from django.contrib import databrowse

from fault_data.models import FaultMode 

databrowse.site.register(FaultMode)

urlpatterns = patterns('',
	url(r'^$', views.data_browse),
	url(r'^all_mode/$', views.browse_all_mode),
	url(r'^syslog/$', views.syslog),
	url(r'^all_cause/$', views.browse_all_cause),
	url(r'^search/$', views.search),
	url(r'^fault_mode/manage_search/$', views.mode_manage_search),
	url(r'^fault_cause/manage_search/$', views.cause_manage_search),
	url(r'^fault_mode/(?P<mode_id>\d+)/$', views.mode_detail),
	url(r'^fault_cause/(?P<cause_id>\d+)/$', views.cause_detail),
	url(r'^diagnose/$', views.diagnose),
	url(r'^diagnose/(?P<mode_id>\d+)/$', views.dgdetail),
	url(r'^fault_mode/del/(?P<mode_id>\d+)/$', views.delmode),
	url(r'^fault_cause/del/(?P<cause_id>\d+)/$', views.delcause),
	url(r'^fault_mode/modify/(?P<mode_id>\d+)/$', views.modifymode),
	url(r'^fault_cause/modify/(?P<cause_id>\d+)/$', views.modifycause),
	url(r'^dfunction/(?P<function_id>\w+)/$', views.dfunction),
	url(r'^fault_mode/modify/(?P<mode_id>\d+)/(?P<attr>\w+)$', views.mode_detailmodify),
	url(r'^fault_cause/modify/(?P<cause_id>\d+)/(?P<attr>\w+)$', views.cause_detailmodify),
	url(r'^manage/$', views.datamanage),
	url(r'^manage_mode_list/$', views.manage_mode_list),
	url(r'^manage_cause_list/$', views.manage_cause_list),
	url(r'^manage_relation_list/$', views.manage_relation_list),
	url(r'^add_mode_data/$', views.add_mode_data),
	url(r'^add_cause_data/$', views.add_cause_data),
	url(r'^add_cause_data/$', views.add_cause_data),
	url(r'^fault_mode/addattr/$', views.add_mode_attr),
#	url(r'^dfunction/(?P<function_id>\d+)/$', views.dfunction, name='function_id'),	
#    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
