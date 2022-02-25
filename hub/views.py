from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from hub.models import Coach, Student

# Create your views here.
def homePage(request):
    return HttpResponse("<h1> Welcome To the home page </h1>")

def students_coach_List(request):
    list = Student.objects.all()
    list2 = Coach.objects.all()
    #select * from student
    return render(
        request,
        'hub/index.html',
        {
            'students': list,
            'coachs' :list2 ,
        }
    )
class StudentListView(ListView):
    model=Student
    template_name="hub/index.html"
    paginate_by = 5

class StudentDetailView(DetailView):
    model=Student


def student_details(request, id):
    student = Student.objects.get(id=id)
    return render (
        request,
        'hub/st_details.html',
        {
            'student': student,
        }
    )
    
