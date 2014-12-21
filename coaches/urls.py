from django.conf.urls import patterns, include, url
from coaches.views import coaches_list, coaches_item, coaches_form, coaches_add


urlpatterns = patterns('',
    url(r'^$', coaches_list, name='coaches_list'),
    url(r'^(?P<coach_id>\d+)/$', coaches_item, name='coaches_item'),
    url(r'^form/(?P<coach_id>\d+)/$', coaches_form, name='coaches_form'),
    url(r'^add/$', coaches_add, name='coaches_add'),
)