from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *

def index(request):
    teacher = TeacherModel()
    student = StudentModel()
    manager = ManagerModel()
    parent = ParentModel()
    return render(request, 'index.html', {'teacher': teacher, 'student': student,
                                          'manager': manager, 'parent': parent})

def addTeacher(request):
    message = ''

    if request.method == 'POST':
        teacher = TeacherModel(request.POST)
        if teacher.is_valid():
            Teacher(
                Username=teacher.data['Username'],
                Password=teacher.data['Password'],
                First_name=teacher.data['FirstName'],
                Last_name=teacher.data['LastName'],
                Phone=teacher.data['Phone'],
                International_code=teacher.data['International_Code'],
                Code_vezarat_olom=teacher.data['Code_vezarat_olom'],
                Work_experience=teacher.data['Work_experience'],
                Education=teacher.data['Education']).save()
            message = 'Teacher added'
            return HttpResponseRedirect('/')
        else:
            message = 'Invalid data'
    else:
        teacher = TeacherModel()

    return render(request, 'index.html', {'message': message})

def addStudent(request):
    message = ''

    if request.method == 'POST':
        student = StudentModel(request.POST)
        if student.is_valid():
            Student(
                Username=student.data['Username'],
                Password=student.data['Password'],
                First_name=student.data['FirstName'],
                Last_name=student.data['LastName'],
                Phone=student.data['Phone'],
                International_code=student.data['International_Code'],
                Education_level=student.data['Education_level'],
                Debt_status=student.data['Debt_status']).save()
            message = 'Student added'
            return HttpResponseRedirect('/')
        else:
            message = 'Invalid data'
    else:
        student = StudentModel()

    return render(request, 'index.html', {'message': message})

def addManager(request):
    message = ''

    if request.method == 'POST':
        manager = ManagerModel(request.POST)
        if manager.is_valid():
            Manager(
                Username=manager.data['Username'],
                Password=manager.data['Password'],
                First_name=manager.data['FirstName'],
                Last_name=manager.data['LastName'],
                Phone=manager.data['Phone'],
                International_code=manager.data['International_Code']).save()
            message = 'Manager added'
            return HttpResponseRedirect('/')
        else:
            message = 'Invalid data'
    else:
        manager = ManagerModel()

    return render(request, 'index.html', {'message': message})

def addParent(request):
    message = ''

    if request.method == 'POST':
        parent = ParentModel(request.POST)
        if parent.is_valid():
            Parent(
                Username=parent.data['Username'],
                Password=parent.data['Password'],
                First_name=parent.data['FirstName'],
                Last_name=parent.data['LastName'],
                Phone=parent.data['Phone'],
                International_code=parent.data['International_Code'],
                Number_of_children=parent.data['Number_of_children']
            ).save()
            message = 'Parent added'
            return HttpResponseRedirect('/')
        else:
            message = 'Invalid data'
    else:
        parent = ParentModel()

    return render(request, 'index.html', {'message': message})
