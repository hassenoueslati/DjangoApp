from django.urls import path

from .views import homePage, student_details, students_coach_List, StudentListView

urlpatterns = [
    path('home/', homePage, name="home"),
    path('index/', students_coach_List, name= 'index'),
    path('index/<int:id>', student_details, name= 'detailstudent'),
    path('ListStudent', StudentListView.as_view(), name= 'student'),

]