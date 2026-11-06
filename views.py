from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            email=request.POST['email'],
            course=request.POST['course'],
            year_level=request.POST['year_level'],
        )
        return redirect('student_list')
    return render(request, 'students/add_student.html')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.firstname = request.POST['firstname']
        student.lastname = request.POST['lastname']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.year_level = request.POST['year_level']
        student.save()
        return redirect('student_list')
    return render(request, 'students/edit_student.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/delete_student.html', {'student': student})