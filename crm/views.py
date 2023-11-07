from django.shortcuts import render,redirect

from django.views.generic import View
# Create your views here.

from crm.forms import EmployeeModelForm
from crm.models import Employees

class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeModelForm()   #model form for models used fields will take
        return render(request,"emp_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()    
            # Employees.objects.create(**form.cleaned_data)
            print("created")
            return render(request,"emp_add.html",{"form":form})
        
        else:
            return render(request,"emp_add.html",{"form":form})
        

#employee list all
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        return render(request,"emp_list.html",{"data":qs})
    
    def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        qs=Employees.objects.filter(name__icontains=name)
        return render(request,"emp_list.html",{"data":qs})

#employee detail view
class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
       # print(kwargs)   so pk values in kwargs so the given value will come as pk:4
        id=kwargs.get("pk")  #pk is given in urls <int:pk>
        qs=Employees.objects.get(id=id)
        return render(request,"emp_detail.html",{"data":qs})

# employee delete view
class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        return redirect("emp-all")
    
#employee update view
class EmployeeUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Employees.objects.get(id=id)
        form=EmployeeModelForm(instance=obj)
        return render(request,"emp_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Employees.objects.get(id=id)
        form=EmployeeModelForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("emp-detail",pk=id)
        else:
            return render(request,"emp_edit.html",{"form":form})