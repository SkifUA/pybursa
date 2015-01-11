from django.conf.urls import patterns, include, url
from coaches.views import CoachList, CoachView, CoachCreatView, CoachUpdateView, CoachDelete
from django.conf.urls import patterns
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', CoachList.as_view(), name='coaches_list'),
    url(r'^(?P<pk>\d+)/$', CoachView.as_view(), name='coaches_item'),
    url(r'^form/(?P<pk>\d+)/$', CoachUpdateView.as_view(), name='coaches_form'),
    url(r'^add/$', CoachCreatView.as_view(), name='coaches_add'),
    url(r'^form/(?P<pk>\d+)/delete/$', CoachDelete.as_view(), name="coach_delete"),
)