
from django.forms.widgets import PasswordInput
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_login(request):
    if request.method =="POST":
        Username = request.POST['Username']
        Password = request.POST['Password']

        user = auth.authenticate(Username=Username,Password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect(request, "employee_register/employee_list.html")
        else:
            messages.info(request,'invalid info')
            return render(request,'employee_register/employee_login.html')
    else:
        return render(request,'employee_register/employee_login.html')

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id ==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

def employee_logout(request):
    auth.logout(request)
    return render(request,'employee_register/employee_login.html')
