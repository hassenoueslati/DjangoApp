from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from hub.forms import StudentForm, StudentModelForm

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
    #paginate_by = 5

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

def StudentCreate(request) :
    #print(request)
    if request.method == 'POST' :
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')

        Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email
        )
        #redirect prend la valeur de nom qui setrouve dans urls 
        return redirect ("student")
        
    return render(
           request,
            'hub/add_student.html'
    )

def StudentCreateForm(request):
    form = StudentForm()
    if request.method =='POST' :
        form = StudentForm(request.POST)
        if form.is_valid():
            # Student.objects.create(
            #     first_name = form.cleaned_data.get('first_name'),
            #     last_name = form.cleaned_data['last_name'],
            #     email = form.cleaned_data['email']
            # )
            Student.objects.create(**form.cleaned_data)
            return redirect('student')

    return render(
            request,
                'hub/add_student.html',
                {
                    'form' : form
                }
        )
 
def add_Student(request) :
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            #traitement
            student.save()
            return redirect('student')

    return render(
            request,
                'hub/add_student.html',
                {
                    'form' : form
                }
        )

class StudentCreateView(CreateView):
    model = Student 
    form_class = StudentModelForm
    template_name= "hub/add_student.html"
    # def get_success_url(self):
    #     return redirect('student')

class StudentUpdateView(UpdateView) :
    model = Student
    form_class = StudentModelForm
    template_name = "hub/add_student.html"

class StudentDeleteView(DeleteView) :
    model = Student
    success_url = reverse_lazy('student')

def student_delete(request, id) :
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student')