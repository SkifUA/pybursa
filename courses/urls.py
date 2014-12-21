from django.conf.urls import patterns, include, url
from courses.views import courses_list, courses_item, courses_form, courses_add


urlpatterns = patterns('',
    url(r'^$', courses_list, name="courses_list"),
    url(r'^(?P<course_id>\d+)/$', courses_item, name="course_item"),
    url(r'^/add$', courses_add, name="courses_add"),
    url(r'^form/(?P<course_id>\d+)/$', courses_form, name="courses_form"),
)