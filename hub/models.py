from django.urls import reverse
from multiprocessing import Value
from this import d
from django.shortcuts import redirect
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
# Create your models here.

def is_Esprit_Email(value):
    if not str(value).endswith('@esprit.tn'):
        raise ValidationError(
            'Your email must be @esprit.tn', params={'value':value})
    return value

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(
        verbose_name="Email", 
        null=False, 
        validators=[is_Esprit_Email, ] 
    ) #de base Chrafield
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Student(User):
    def get_absolute_url(self):
        return reverse('student')
    
    pass
class Coach(User):
    pass
class Projet(models.Model):
    project_name=models.CharField(max_length=50)
    dure=models.IntegerField()
    temp_allocated=models.IntegerField(validators=[MinValueValidator(1,"le temps min doit etre 1 heure"),
    MaxValueValidator(5,"le temps max doit etre 5 heure")
    ])
    besoin=models.TextField(max_length=250)
    description=models.TextField(max_length=250)
    isValid=models.BooleanField(default=False)
    creator=models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='creators'
    )
    supervisor=models.ForeignKey(
        Coach,
        on_delete=models.CASCADE, #en cas ou en supprime le user ,l'attribut va etre null
        related_name='supervisors'
    )
    member=models.ManyToManyField(
        Student,
        through='MemberShip' ,
        related_name='membres'   
    ) #il va genere une classe intermidiare nommé membreShip
    def __str__(self) -> str:
        return f"{self.project_name}"
class MemberShip(models.Model):
    projet=models.ForeignKey(
        Projet,
        on_delete=models.CASCADE,
        related_name='memberships'
    )
    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='students'
    )
    allocated_time_by_member=models.IntegerField(default=0)