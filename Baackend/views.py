from django.shortcuts import render, redirect

import Frontend.views
from Frontend.models import EmployeeDB, LoginDB
from Baackend.models import TaskDB
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate



# Create your views here.
def admin_page(req):
    return render(req, "admin_page.html")


def employee_details(req):
    data = LoginDB.objects.all()
    return render(req, "employees.html", {'data': data})


def assign_task_page(req):
    data = EmployeeDB.objects.all()
    return render(req, "task.html", {'data': data})


def assign_task(req):
    if req.method == "POST":
        en = req.POST.get('emp_name')
        tsk = req.POST.get('task')
        tsk_dsc = req.POST.get('task_desc')
        st = req.POST.get('status')
        dt = req.POST.get('dead_line')

        task_obj = TaskDB(EmployeeName=en, Task=tsk, TaskDescription=tsk_dsc, DeadLine=dt, Status=st)
        task_obj.save()
        messages.success(req, "Task Assigned")
        return redirect(assign_task_page)


def view_task(req,emp_name):
    data = TaskDB.objects.filter(EmployeeName=emp_name)
    return render(req, "viewtask.html", {'data': data})


def view_all_task(req):
    data = TaskDB.objects.all()
    return render(req, "alltask.html", {'data': data})


def remove_task(req, emp_id):
    data = TaskDB.objects.filter(id=emp_id)
    data.delete()
    messages.info(req, "Task Removed..!")
    return redirect(view_all_task)


# def admin_login_page(req):
#     return render(req, "adminlogin.html")


# def admin_login_validate(req):
#     if req.method == "POST":
#         un = req.POST.get('u_name')
#         psd = req.POST.get('password')
#
#         if User.objects.filter(username__contains=un).exists():
#             x = authenticate(username=un, password=psd)
#             if x is not None:
#                 login(req, x)
#                 req.session['Username']=un
#                 req.session['Password']=psd
#
#                 messages.success(req, "Welcome..!")
#                 return redirect(admin_page)
#             else:
#                 messages.error(req, "Invalid Credentials..!")
#                 return redirect(admin_login_page)
#         else:
#             messages.error(req, "Please Check your Username...!")
#             return redirect(admin_login_page)


def admin_logout(req):
    del req.session['Username']
    del req.session['Password']
    messages.info(req, "Logged out")
    return redirect(Frontend.views.login_page)
