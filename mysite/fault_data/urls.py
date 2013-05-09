
from django.conf.urls import patterns, url

from fault_data import views

from django.contrib import databrowse

from fault_data.models import FaultMode 

databrowse.site.register(FaultMode)

urlpatterns = patterns('',
	(r'^databrowse/(.*)', databrowse.site.root),
	url(r'^$', views.databrose),
	url(r'^all_mode/$', views.broseallmode),
	url(r'^all_cause/$', views.broseallcause),
	url(r'^search-form/$', views.search_form),
	url(r'^search/$', views.search),
	url(r'^manage_search/$', views.manage_search),
	url(r'^(?P<mode_id>\d+)/$', views.detail),
	url(r'^diagnose/$', views.diagnose),
	url(r'^diagnose/(?P<mode_id>\d+)/$', views.dgdetail),
	url(r'^del/(?P<mode_id>\d+)/$', views.delmode),
	url(r'^modify/(?P<mode_id>\d+)/$', views.modifymode),
	url(r'^dfunction/(?P<function_id>\w+)/$', views.dfunction),
	url(r'^modify/(?P<mode_id>\d+)/(?P<attr>\w+)$', views.detailmodify),
	url(r'^manage/$', views.datamanage),
	url(r'^manage_list/$', views.managelist),
	url(r'^add_data/$', views.add_data),
	url(r'^addattr/$', views.addattr),
#	url(r'^dfunction/(?P<function_id>\d+)/$', views.dfunction, name='function_id'),	
#    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
