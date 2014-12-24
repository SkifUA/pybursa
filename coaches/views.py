from django import forms

from coaches.models import Coach
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


class CoachModelForm(forms.ModelForm):
    
    class Meta:
        model = Coach


class CoachList(ListView):
    template_name = "coaches/list.html"
    model = Coach
    context_object_name = "coaches"

    
class CoachView(DetailView):
    template_name = "coaches/item.html"
    model = Coach
    context_object_name = "coach"


class CoachCreatView(CreateView):
    template_name = 'coaches/form.html'
    form_class = CoachModelForm 
    model = Coach
    success_url = '/coaches/'

    def get_context_data(self, **kwargs):
        context = super(CoachCreatView, self).get_context_data(**kwargs)
        context['title'] = "Create item"
        return context


class CoachUpdateView(UpdateView):
    template_name = 'coaches/form.html'
    form_class = CoachModelForm 
    model = Coach
    success_url = '/coaches/'

    def get_context_data(self, **kwargs):
        context = super(CoachUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Edit item"
        return context


class CoachDelete(DeleteView):
    model = Coach
    success_url = '/coaches/'

    
