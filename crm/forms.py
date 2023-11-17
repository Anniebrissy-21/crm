from django import forms
from crm.models import Employees
from django.contrib.auth.models import User

# class EmployeesForm(forms.Form):

#     name=forms.CharField()
#     department=forms.CharField()
#     salary=forms.IntegerField()
#     email=forms.EmailField()
#     age=forms.IntegerField()
#     contacts=forms.CharField()

class EmployeeModelForm(forms.ModelForm):   #form is taken from models so views dont need to create orm query
    class Meta:
        model=Employees
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control mt-2"}),
            "department":forms.TextInput(attrs={"class":"form-control mt-2"}),
            "salary":forms.NumberInput(attrs={"class":"form-control mt-2"}),
            "email":forms.EmailInput(attrs={"class":"form-control mt-2"}),
            "age":forms.NumberInput(attrs={"class":"form-control mt-2"}),
            "contacts":forms.Textarea(attrs={"class":"form-control mt-2","rows":5}),
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})

        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mt-3"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mt-3"}))

    

    