from django import forms
from crm.models import Employees

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
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "contacts":forms.Textarea(attrs={"class":"form-control","rows":5})
        }