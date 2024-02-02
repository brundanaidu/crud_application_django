from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

def index(request):
    students = Student.objects.all()

    context = {'students': students}

    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']

        data = Student(name=name, age=age, email=email)
        data.save()
        return redirect('index')

    return render(request, 'create.html')

def delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('index')

def edit(request, pk):
    edit_student = Student.objects.get(id=pk)

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']

        edit_data = Student(id=pk, name=name, age=age, email=email)
        edit_data.save()
        return redirect('index')

    context = {'edit_student': edit_student}
    return render(request, 'edit.html', context)