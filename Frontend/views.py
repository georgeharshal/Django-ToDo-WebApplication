from django.shortcuts import render, redirect
from Frontend.models import EmployeeDB, LoginDB
from Baackend.models import TaskDB
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from Baackend.views import admin_page

from django.contrib import messages

import datetime

# Create your views here.
def index_page(req):
    if 'Username' in req.session:
        data = TaskDB.objects.filter(EmployeeName=req.session['Username'])
        return render(req, "index.html", {'data': data})
    else:
        return render(req, "index.html")

def signup_page(req):
    return render(req, "SignUp.html")


def login_page(req):
    return render(req, "LogIn.html")


def user_signup(req):
    if req.method == "POST":
        un = req.POST.get('u_name')
        em = req.POST.get('email')
        ps = req.POST.get('pswd')
        c_ps = req.POST.get('cnf_pswd')
        if len(ps) < 8:
            messages.warning(req, "WeakPassword")
            return redirect(signup_page)
        elif ps != c_ps:
            messages.error(req, "Passwords does not match")
            return redirect(signup_page)
        else:
            Emp_OBJ = EmployeeDB(Name=un, EmailId=em, Password=ps)
            Emp_OBJ.save()
            messages.success(req, "User Registered")
            return redirect(login_page)


def login_validate(req):
    if req.method == "POST":
        un = req.POST.get('u_name')
        ps = req.POST.get('pswd')

        if EmployeeDB.objects.filter(Name=un, Password=ps).exists():
            req.session['Username'] = un
            req.session['Password'] = ps
            em = EmployeeDB.objects.get(Name=un).EmailId
            lgn = datetime.datetime.now()
            if LoginDB.objects.filter(Name=un).exists():
                LoginDB.objects.filter(Name=un).update(Name=un, EmailId=em, LastLogin=lgn)
            else:
                login_OBJ = LoginDB(Name=un, EmailId=em, LastLogin=lgn)
                login_OBJ.save()

            messages.success(req, "Logged In")
            return redirect(index_page)
        elif User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=ps)
            if x is not None:
                login(req, x)
                req.session['Username']=un
                req.session['Password']=ps

                messages.success(req, "Welcome..!")
                return redirect(admin_page)
            else:
                messages.error(req, "Invalid Credentials..!")
                return redirect(login_page)
        else:
            messages.error(req, "Incorrect Credentials")
            return redirect(login_page)
    else:
        messages.warning(req, "Enter a valid username")
        return redirect(login_page)


def user_logout(req):
    del req.session['Username']
    del req.session['Password']
    messages.info(req, "Logged out")
    return redirect(login_page)




def update_task(req, task_id):
    if req.method == "POST":

        st = req.POST.get('status')

        TaskDB.objects.filter(id=task_id).update(Status=st)

        messages.success(req, "Task Completed")
        return redirect(index_page)







