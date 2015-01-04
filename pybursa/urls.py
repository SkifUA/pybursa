from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import send_message


urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^students/', include('students.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^abuses/', include('abuses.urls')),
    url(r'^send/$',send_message , name='send-message'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)
