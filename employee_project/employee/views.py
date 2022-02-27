from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()
    context = {
        'employee_list' : employees
    }
    return render(request, 'employee/employee_list.html',context)

def employee_form(request, id = 0):
    if request.method == 'GET':
        if id == 0 :
            form = EmployeeForm()
        else: 
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        context = {
            'form' : form
        }
        return render(request, 'employee/employee_form.html',context)        
        
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

 

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')



     