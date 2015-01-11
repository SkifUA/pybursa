from django import forms

from coaches.models import Coach
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.shortcuts import redirect
from datetime import datetime, date
import logging
logger = logging.getLogger(__name__)


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
    #success_url = '/coaches/'

    def get_context_data(self, **kwargs):
        context = super(CoachCreatView, self).get_context_data(**kwargs)
        context['title'] = "Create item"
        return context

    def form_valid(self, form):
        obj=form.save()
        logger.debug(str(datetime.today()) + ":courses-DEBUG-add coache id= " + str(obj.id))
        return redirect('coaches_list')


class CoachUpdateView(UpdateView):
    template_name = 'coaches/form.html'
    form_class = CoachModelForm 
    model = Coach
    success_url = '/coaches/'

    def get_context_data(self, **kwargs):
        context = super(CoachUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Edit item"
        return context

    def form_valid(self, form):
        obj=form.save()
        logger.debug(str(datetime.today()) + ":courses-DEBUG-edit coache id= " + str(obj.id))
        return redirect('coaches_list')


class CoachDelete(DeleteView):
    model = Coach
    success_url = '/coaches/'

    
