from django.shortcuts import render, redirect
from courses.models import Course

from django import forms

class CourseModelForm(forms.ModelForm):
    ''' make form for add new row '''
    class Meta:
        model = Course

class CourseForm(forms.Form):
    COURS_LIST = (
        ('python', 'python'),
        ('JS', 'JS'), 
        ('rubybursa', 'rubybursa')
        )
    course_name = forms.CharField(max_length=100)
    course_tehnology = forms.ChoiceField(widget=forms.RadioSelect, choices=COURS_LIST)
    course_slug = forms.CharField(max_length=100)
    course_description = forms.CharField(max_length=100)
    course_teacher = forms.CharField(max_length=100)
    course_assistent = forms.CharField(max_length=100)
    course_date_start = forms.DateField()
    course_date_end = forms.DateField()



def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})


def courses_item(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/item.html', {'course': course})

def courses_form(request, course_id):

    course = Course.objects.get(id=course_id)

    title = "Edit item"
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course.name = form.cleaned_data ['course_name']
            course.tehnology = form.cleaned_data ['course_tehnology']
            course.slug = form.cleaned_data ['course_slug']
            course.description = form.cleaned_data ['course_description']
            course.teacher = form.cleaned_data ['course_teacher']
            course_assistent = form.cleaned_data ['course_assistent']
            course.date_start = form.cleaned_data ['course_date_start']
            course.date_end = form.cleaned_data ['course_date_end']
			
            course.save()
            #print form.cleaned_data
            return redirect('courses_form', course.id)       
    else:
        form = CourseForm(initial={'course_name': course.name, 
                                  'course_tehnology': course.tehnology, 
                                  'course_slug': course.slug, 
                                  'course_description': course.description, 
                                  'course_teacher': course.teacher,
                                  'course_assistent': course.assistent,
                                  'course_date_start': course.date_start,
                                  'course_date_end': course.date_end,
                                   })
       
    return render(request, 'courses/form.html', {'form': form, 'title': title})


def courses_add(request):

    title = "Add item"
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            
            coach = form.save()
            return redirect('courses_form', coach.id)       
    else:
        form = CourseModelForm()

    return render(request, 'courses/form.html', {'form': form, 'title': title})



#def courses_add(request):
#    title = "Add item"
#    if request.method == 'POST':
#        form = CourseForm(request.POST)
#        if form.is_valid():
#            course = form.cleaned_data
#            print course
#            course.save()
#            return redirect('courses_form', course.id)       
#    else:
#        form = CourseForm()
#     
#    return render(request, 'courses/form.html', {'form': form, 'title': title})


	

