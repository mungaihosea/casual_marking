from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as login_user, logout as logout_user
from django.contrib.auth.models import User
from .models import Marker, Student, Task


#check account type
def check_account_type(user):
    students = list(Student.objects.values_list('username', flat = True))
    markers =  list(Marker.objects.values_list('username', flat = True))
    if students.__contains__(user.username):
        return 'student'
    elif markers.__contains__(user.username):
        return 'marker'


#handles login
def index(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        try:
            user = User.objects.get(username = username)
            if user.check_password(user):
                login_user(request, user)
                if user.is_superuser:
                    return redirect('admin_page')
                elif check_account_type(user) == 'student':
                    return redirect('student_page')
                elif check_account_type(user) == 'marker':
                    return redirect('marker_page')
        except Exception as e:
            print(e)

    return render(request, "index.html", {})

#use this form to create accounts
def admin(request, success = None):
    return render(request, "admin.html", {"success": success})

#create a student instance
def create_student(request):
    if request.method == "POST":
        student = Student()
        student.username = request.POST.get('username', None)
        student.set_password(request.POST.get('password'))
        student.save()
        return admin(request, success="student account created successfully")
    return redirect('admin_page')
    
    
#create a marker instance
def create_marker(request):
    if request.method == "POST":
        marker = Marker()
        marker.username = request.POST.get('username', None)
        marker.set_password(request.POST.get('password'))
        marker.save()
        
        return admin(request, success="Lecturer account created successfully")
    return redirect('admin_page')


#use this form to submit assingments for marking
def student(request):
    return render(request, 'student_page.html', {})

#handles marking of assignments
def marker(request):
    marker = get_object_or_404(Marker, username = request.user.username)
    Task.objects.filter(marker = marker)
    return render(request, 'marker_page.html', {})