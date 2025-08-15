from django.shortcuts import render, HttpResponse, redirect

def home(request):
    return render(request, 'hemmo.html')


# Create your views here.
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Department, Faculty 

from django.shortcuts import render, get_object_or_404
from .models import Department, Faculty

def faculty_list(request, dept_name=None):
    """
    If dept_name is given, show only faculty of that department.
    Otherwise, show all departments.
    """
    if dept_name:
        department = get_object_or_404(Department, name__iexact=dept_name)
        faculty = Faculty.objects.filter(department=department).order_by('-experience_years')
        departments = [department]  # To keep template loop simple
    else:
        departments = Department.objects.all()
        faculty = Faculty.objects.all().order_by('-experience_years')
    
    context = {
        'departments': departments,
        'faculty': faculty,
    }
    return render(request, 'faculty_list.html', context)

def faculty_by_department(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    faculty = department.faculty_members.all().order_by('-experience_years')
    return render(request, 'faculty_by_department.html', {
        'department': department,
        'faculty': faculty
    })
