from django.urls import path

from .views import StudentCreateForm, StudentCreateView, add_Student, homePage, student_details, StudentCreate, students_coach_List, StudentListView

urlpatterns = [
    path('home/', homePage, name="home"),
    path('index/', students_coach_List, name= 'index'),
    path('index/<int:id>', student_details, name= 'detailstudent'),
    path('ListStudent', StudentListView.as_view(), name= 'student'),
    path('addStudent',StudentCreate, name='addstudent'),
    path('addStudent2',StudentCreateForm, name='addStudent2'),
    path('addStudent3',add_Student, name='addStudent3'),
    path('addStudent4',StudentCreateView.as_view(), name='addStudent4')

]