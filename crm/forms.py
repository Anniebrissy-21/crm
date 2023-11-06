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

    