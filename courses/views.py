from django import forms

from courses.models import Course
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


class CourseModelForm(forms.ModelForm):
    
    class Meta:
        model = Course
        #widgets = {'tehnology': forms.RadioSelect}


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
    success_url = '/courses/'

    def get_context_data(self, **kwargs):
        #print kwargs
        context = super(CourseCreatView, self).get_context_data(**kwargs)
        context['title'] = "Create item"
        return context
    

class CourseUpdateView(UpdateView):
    template_name = 'courses/form.html'
    form_class = CourseModelForm 
    model = Course
    success_url = '/courses/'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Edit item"
        return context


class CourseDelete(DeleteView):
    model = Course
    success_url = '/courses/'




	

