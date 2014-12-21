from django.shortcuts import render, redirect
from coaches.models import Coach

from django import forms

class CoachModelForm(forms.ModelForm):
    ''' make form for add new row '''
    class Meta:
        model = Coach


def coaches_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/list.html', {'coaches': coaches})


def coaches_item(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    return render(request, 'coaches/item.html', {'coach': coach})


def coaches_form(request, coach_id):

	coach = Coach.objects.get(id=coach_id)
	title = "Edit item"
	if request.method == 'POST':
		form = CoachModelForm(request.POST, instance=coach)
		if form.is_valid():
			coach = form.save()
			return redirect('coaches_form', coach.id)       
	else:
		form = CoachModelForm(instance=coach)
       
	return render(request, 'coaches/form.html', {'form': form, 'title': title})


def coaches_add(request):

    title = "Add item"

    if request.method == 'POST':
        form = CoachModelForm(request.POST)
        if form.is_valid():
        	
            coach = form.save()
            return redirect('coaches_form', coach.id)       
    else:
        form = CoachModelForm()

    return render(request, 'coaches/form.html', {'form': form, 'title': title})