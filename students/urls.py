from django.conf.urls import patterns, include, url
from students.views import students_list, students_item


urlpatterns = patterns('',
    url(r'^$', students_list, name="students_list"),
    url(r'^(?P<student_id>\d+)/$', students_item, name="students_item"),
)
