from django.conf.urls import patterns, include, url
from students.views import students_list, students_item, students_form, students_new, students_delete


urlpatterns = patterns('',
    url(r'^$', students_list, name="students_list"),
    url(r'^form/(?P<student_id>\d+)/$', students_form, name="students_form"),
    url(r'^new/$', students_new, name="students_new"),
    url(r'^(?P<student_id>\d+)/$', students_item, name="students_item"),
    url(r'^form/(?P<student_id>\d+)/delete/$', students_delete, name="students_delete"),
)
