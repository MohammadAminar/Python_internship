from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ManagerModel, ParentModel, StudentModel, TeacherModel
from .models import Manager, Parent, Student, Teacher


def teachers(request):
    teacher = TeacherModel()

    teachers = Teacher.objects.all()

    return render(request, 'User/Teacher/teacher.html', context={'teacher': teacher, 'teachers': teachers})


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
            return HttpResponseRedirect('/teachers')
        else:
            message = 'Invalid data'  # noqa: F841
    else:
        teacher = TeacherModel()

    return render(request, 'User/Teacher/teacher.html')


def EditTeacher(request):
    if request.method == 'POST':
        teacher = TeacherModel(request.POST)
        id = teacher.data['User_Id']
        result = Teacher.objects.filter(User_Id=id).first()
        result.First_name = teacher.data['FirstName']
        result.Last_name = teacher.data['LastName']
        result.Phone = teacher.data['Phone']
        result.International_code = teacher.data['International_Code']
        result.Username = teacher.data['Username']
        result.Password = teacher.data['Password']
        result.Work_experience = teacher.data['Work_experience']
        result.Education = teacher.data['Education']
        result.save()
        return HttpResponseRedirect('/teachers')


def DeleteTeacher(request, id):
    result = Teacher.objects.filter(User_Id=id).first()
    result.delete()
    return HttpResponseRedirect('/teachers')


def students(request):
    student = StudentModel()

    students = Student.objects.all()

    return render(request, 'User/Student/student.html', context={'student': student, 'students': students})


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
            return HttpResponseRedirect('/students')
        else:
            message = 'Invalid data'
    else:
        student = StudentModel()

    return render(request, 'User/Student/student.html', {'message': message})


def EditStudent(request):
    if request.method == 'POST':
        student = StudentModel(request.POST)
        id = student.data['User_Id']
        result = Student.objects.filter(User_Id=id).first()
        result.First_name = student.data['FirstName']
        result.Last_name = student.data['LastName']
        result.Phone = student.data['Phone']
        result.International_code = student.data['International_Code']
        result.Username = student.data['Username']
        result.Password = student.data['Password']
        result.Education_level = student.data['Education_level']
        result.Debt_status = student.data['Debt_status']
        result.save()
        return HttpResponseRedirect('/students')


def DeleteStudent(request, id):
    result = Student.objects.filter(User_Id=id).first()
    result.delete()
    return HttpResponseRedirect('/students')


def managers(request):
    manager = ManagerModel()

    managers = Manager.objects.all()

    return render(request, 'User/Manager/manager.html', context={'manager': manager, 'managers': managers})


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
            return HttpResponseRedirect('/managers')
        else:
            message = 'Invalid data'
    else:
        manager = ManagerModel()

    return render(request, 'User/Manager/manager.html', {'message': message})


def EditManager(request):
    if request.method == 'POST':
        manager = ManagerModel(request.POST)
        id = manager.data['User_Id']
        result = Manager.objects.filter(User_Id=id).first()
        result.First_name = manager.data['FirstName']
        result.Last_name = manager.data['LastName']
        result.Phone = manager.data['Phone']
        result.International_code = manager.data['International_Code']
        result.Username = manager.data['Username']
        result.Password = manager.data['Password']
        result.save()
        return HttpResponseRedirect('/managers')


def deleteManager(request, id):
    result = Manager.objects.filter(User_Id=id).first()
    result.delete()
    return HttpResponseRedirect('/managers')


def parents(request):
    parent = ParentModel()

    parents = Parent.objects.all()

    return render(request, 'User/Parent/parent.html', context={'parent': parent, 'parents': parents})


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
            return HttpResponseRedirect('/parents')
        else:
            message = 'Invalid data'
    else:
        parent = ParentModel()

    return render(request, 'User/Parent/parent.html', {'message': message})


def EditParent(request):
    if request.method == 'POST':
        parent = ParentModel(request.POST)
        id = parent.data['User_Id']
        result = Parent.objects.filter(User_Id=id).first()
        result.First_name = parent.data['FirstName']
        result.Last_name = parent.data['LastName']
        result.Phone = parent.data['Phone']
        result.International_code = parent.data['International_Code']
        result.Username = parent.data['Username']
        result.Password = parent.data['Password']
        result.Number_of_children = parent.data['Number_of_children']
        result.save()
        return HttpResponseRedirect('/parents')


def deleteParent(request, id):
    result = Parent.objects.filter(User_Id=id).first()
    result.delete()
    return HttpResponseRedirect('/parents')
