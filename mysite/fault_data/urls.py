
from django.conf.urls import patterns, url

from fault_data import views

from django.contrib import databrowse

from fault_data.models import FaultMode 

databrowse.site.register(FaultMode)

urlpatterns = patterns('',
	(r'^databrowse/(.*)', databrowse.site.root),
	url(r'^$', views.databrose, name='databrose'),
	url(r'^search-form/$', views.search_form),
	url(r'^search/$', views.search),
	url(r'^(?P<mode_id>\d+)/$', views.detail, name='detail'),
	url(r'^diagnose/$', views.diagnose, name='diagnose'),
	url(r'^diagnose/(?P<mode_id>\d+)/$', views.dgdetail, name='dgdetail'),
	url(r'^dfunction/(?P<function_id>\w+)/$', views.dfunction, name='function_id'),
#	url(r'^dfunction/(?P<function_id>\d+)/$', views.dfunction, name='function_id'),	
#    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
