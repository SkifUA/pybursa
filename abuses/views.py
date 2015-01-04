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


class AbuseModelForm(forms.ModelForm):
    
    class Meta:
        model = Abuse


class AbuseFormView(FormView):
    template_name = 'abuses/form.html'
    form_class = AbuseModelForm 
    model = Abuse 
    success_url = 'abuses/add/' 

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
        messages.success(self.request, _('Message was send.'))
        return redirect('abuses_add')

        

    
#class MessageForm(forms.Form):
#    email = forms.EmailField()
#    theme = forms.CharField(max_length=200)
#    body = forms.CharField(widget=forms.Textarea)

#def send_message(request):
#    if request.method == 'POST':
#        form = MessageForm(request.POST)
#        if form.is_valid():
#            email = form.cleaned_data['email']
#            theme = form.cleaned_data['theme']
#            body = form.cleaned_data['body']

#            send_mail(theme, body, email, ['test_django@mail.ru'])
#            messages.success(request,'Message was send.')
#            return redirect('send_message')
            
#    else:
#        form = MessageForm()

#    return render(request, 'abuses/form.html', {'form': form})


#def start_message(request):
    #student = Student.objects.get(id=student_id)
    #student = get_object_or_404(Student, id=student_id) 
#    return render(request, 'abuses/start.html')