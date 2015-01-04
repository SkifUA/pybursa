from django import forms
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

class MessageForm(forms.Form):
    email = forms.EmailField()
    theme = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            theme = form.cleaned_data['theme']
            body = form.cleaned_data['body']

            send_mail(theme, body, email, ['realdjango@bigmir.net'])
            messages.success(recuest,'Message was send.')
            return redirect('send-message')
    else:
        form = MessageForm()

    return render(request, 'form.html', {'form': form})
