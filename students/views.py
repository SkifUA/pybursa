from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student

from django import forms


class StudentModelForm(forms.ModelForm):
    ''' make form for add and edit using Model '''
    class Meta:
        model = Student
        prepopulated_fields = {"slug": ("name",)}


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def students_item(request, student_id):
    #student = Student.objects.get(id=student_id)
    student = get_object_or_404(Student, id=student_id) 
    return render(request, 'students/item.html', {'student': student})

def students_form(request, student_id):
    #student = Student.objects.get(id=student_id)
    student = get_object_or_404(Student, id=student_id) 
    title = "Edit item"

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('students_form', student.id)       
    else:
        form = StudentModelForm(instance=student)
       
    return render(request, 'students/form.html', {'form': form, 'title': title})


def students_new(request):
    title = "Add item"
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('students_form', student.id)       
    else:
        form = StudentModelForm()

    return render(request, 'students/add.html', {'form': form, 'title': title})


def students_delete(request, student_id):
    
    Student.objects.get ( id=student_id ).delete() 
        
    return redirect('students_list')