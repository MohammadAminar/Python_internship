from django.urls import path
from . import views

urlpatterns = [
    # Teacher
    path('teachers', views.teachers, name='Teacher'),
    path('addTeacher', views.addTeacher, name='AddTeacher'),
    path('editTeacher', views.EditTeacher, name='EditTeacher'),
    path('Save_Teacher', views.save_Teacher, name='EditTeacher'),
    path('deleteTeacher/<int:id>', views.DeleteTeacher, name='DeleteTeacher'),

    # Student
    path('students', views.students, name='Students'),
    path('addStudent', views.addStudent, name='AddStudent'),
    path('editStudent', views.EditStudent, name='EditStudent'),
    path('deleteStudent/<int:id>', views.DeleteStudent, name='DeleteStudent'),

    # Manager
    path('managers', views.managers, name='Manager'),
    path('addManager', views.addManager, name='AddManager'),
    path('editManager', views.EditManager, name='EditManager'),
    path('deleteManager/<int:id>', views.deleteManager, name='DeleteManager'),

    # Parent
    path('parents', views.parents, name='Parent'),
    path('addParent', views.addParent, name='AddParent'),
    path('editParent', views.EditParent, name='EditParent'),
    path('deleteParent/<int:id>', views.deleteParent, name='DeleteParent'),
]
