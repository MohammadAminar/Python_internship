from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Teacher'),
    path('addTeacher', views.addTeacher, name='AddTeacher'),
    path('addStudent', views.addStudent, name='AddStudent'),
    path('addManager', views.addManager, name='AddManager'),
    path('addParent', views.addParent, name='AddParent'),
]
