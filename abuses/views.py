# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render, redirect 
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from abuses.models import Abuse
from django.views.generic.edit import FormView
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, date
import logging
logger = logging.getLogger(__name__)


class AbuseModelForm(forms.ModelForm):
    
    class Meta:
        model = Abuse


class AbuseFormView(FormView):
    template_name = 'abuses/form.html'
    form_class = AbuseModelForm 
    model = Abuse 
    #success_url = 'abuses/add/' 

    def form_valid(self, form):
        obj=form.save()

        email = form.cleaned_data['email']
        theme = form.cleaned_data['text']
        
        courses_name = str(obj.courses)
        teacher_name = str(obj.name)
        student_name = str(obj.surname)
        
        text =  'Уважаемый ' + teacher_name + '! Сообщаю, что \
         ' + student_name #+ ' ' + theme #+ '. Ваш студент.'

        send_mail(theme, text, email, ['django_test@mail.ru'])
        logger.debug(str(datetime.today()) + ":abuses-DEBUG-send message to " + teacher_name)
        messages.success(self.request, _('Message was send.'))
        
        return redirect('abuses_add')
        