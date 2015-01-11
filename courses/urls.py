from django.conf.urls import patterns, include, url
from courses.views import CourseList, CourseView, CourseCreatView, CourseUpdateView, CourseDelete
from django.conf.urls import patterns
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', CourseList.as_view(), name="courses_list"),
    url(r'^(?P<pk>\d+)/$', CourseView.as_view(), name="course_item"),
    url(r'^/add$', CourseCreatView.as_view(), name="courses_add"),
    url(r'^form/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name="courses_form"),
    url(r'^form/(?P<pk>\d+)/delete/$', CourseDelete.as_view(), name="course_delete"),
    
)