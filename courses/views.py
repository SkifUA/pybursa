from django import forms
from django.shortcuts import redirect 
from courses.models import Course
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from datetime import datetime, date
import logging
logger = logging.getLogger(__name__)


class CourseModelForm(forms.ModelForm):
    
    class Meta:
        model = Course
      


class CourseList(ListView):
    template_name = "courses/list.html"
    model = Course
    #queryset = Course.objects.filter(tehnology='JS')
    context_object_name = "courses"

    
class CourseView(DetailView):
    template_name = "courses/item.html"
    model = Course
    context_object_name = "course"


class CourseCreatView(CreateView):
    template_name = 'courses/form.html'
    form_class = CourseModelForm 
    model = Course
    #success_url = '/courses/'

    def get_context_data(self, **kwargs):
        context = super(CourseCreatView, self).get_context_data(**kwargs)
        context['title'] = "Create item"
        return context

    def form_valid(self, form):
        obj=form.save()
        logger.debug(str(datetime.today()) + ":courses-DEBUG-add course id= " + str(obj.id))
        return redirect('courses_list')
    

class CourseUpdateView(UpdateView):
    template_name = 'courses/form.html'
    form_class = CourseModelForm 
    model = Course
    success_url = '/courses/'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Edit item"
        return context

    def form_valid(self, form):
        obj=form.save()
        logger.debug(str(datetime.today()) + ":courses-DEBUG-edit course id= " + str(obj.id))
        return redirect('courses_list')


class CourseDelete(DeleteView):
    model = Course
    success_url = '/courses/'
    #logger.warning(str(datetime.today()) + ":courses-DEBUG-delete course id= " #+ str(obj.id))

    def form_valid(self, form):
        obj=object.save()
        logger.warning(str(datetime.today()) + ":courses-WARNING-delete course id= " + str(obj.id))
        return redirect('courses_list')




	

