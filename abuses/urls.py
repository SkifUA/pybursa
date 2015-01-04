from django.conf.urls import patterns, include, url
from abuses.views import AbuseFormView#, start_message, send_message

#from django.views.generic import TemplateView


urlpatterns = patterns('',
	#url(r'^$',start_message, name='start_message'),
	#url(r'^send/$',send_message , name='send_message'),
    url(r'^add/$', AbuseFormView.as_view(), name="abuses_add"),
    
     
)