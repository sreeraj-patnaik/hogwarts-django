from django.shortcuts import render
from django.db.models import Case, When, IntegerField
from .models import Faculty

def home(request):
    return render(request, 'base.html')


from django.shortcuts import render
from .models import Faculty

def faculty_list(request):
    """
    Display faculty sorted meaningfully:
    1. Grouped by number of roles (more roles together).
    2. Within each group, sort by sum of role priorities (lower = higher importance).
    3. Tie-breaker = experience_years descending.
    """
    # Define role priority mapping
    role_priority = {
        'Headmaster': 0,
        'Dy Headmistress': 1,
        'Dean': 2,
        'HoD': 3,
        'Professor': 4,
        'Associate Professor': 5,
        'Assistant Professor': 6,
        'Visiting Faculty': 7,
        'Lecturer': 8,
    }
from django.shortcuts import render
from .models import Faculty

def faculty_list(request):
    # Role priority mapping
    role_priority = {
        'Headmaster': 0,
        'Dy Headmistress': 1,
        'Registrar': 2,
        'Dean-Placements': 3,
        'Dean-Research & Development': 3,
        'Dean-Academics': 3,
        'Dean-Administration': 3,
        'Acad. Associate Dean-Student Affairs': 4,
        'Admin. Associate Dean-Faculty Affairs': 4,
        'Acad. Associate Dean-Curriculum': 4,
        'Admin. Associate Dean-Magic and Safety': 4,
        'Controller of Examinations': 3,
        'Deputy Registrar': 5,
        'Assistant Controller of Examinations': 6,
        'HoD': 6,
        'Professor': 7,
        'Associate Professor': 8,
        'Assistant Professor': 9,
        'Visiting Faculty': 10,
        'Lecturer': 11,
    }

    faculty = list(Faculty.objects.all())

    # Helper function to generate a sorted priority tuple for each faculty
    def role_tuple(fac):
        # sort roles by priority ascending
        sorted_roles = sorted([role_priority.get(role, 99) for role in fac.roles])
        return tuple(sorted_roles)

    # Custom comparison key
    def sort_key(f):
        # Absolute first for HM
        if 'Headmaster' in f.roles:
            return (-1, )  # always first
        # Absolute second for DyHM
        if 'Dy Headmistress' in f.roles:
            return (0, )
        # For others: return tuple of (primary_role_priority, secondary_role_priority, ..., -experience)
        # We reverse the role tuple so that more roles matter (longer tuples come first)
        rt = role_tuple(f)
        # prepend a negative length to prioritize more roles
        return (rt[0], -len(rt), rt[1:] if len(rt) > 1 else (), -f.experience_years)

    # Sort faculty using the custom key
    faculty_sorted = sorted(faculty, key=sort_key)

    return render(request, "faculty_list.html", {"faculty": faculty_sorted})

# views.py
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from .forms import UploadFileForm  # Form with `file = FileField()`

from django.shortcuts import render, redirect
from django.contrib import messages
from decimal import Decimal, InvalidOperation
import pandas as pd
from .models import Student
from .forms import UploadFileForm  # simple form with FileField

SEMESTER_SUBS = 8  # number of subjects per semester

def upload_results(request):
    """
    Upload student results via Excel file, update semester subjects, grades, SGPA and CGPA.
    """
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        sem = request.POST.get("semester", "").strip().lower()  # e.g., 'sem1'

        if sem not in [f"sem{i}" for i in range(1, 9)]:
            messages.error(request, "Invalid semester. Use sem1 to sem8.")
            return redirect("upload_results")

        sem_num = int(sem[-1])  # extract semester number as integer

        if form.is_valid():
            try:
                file = request.FILES["file"]
                df = pd.read_excel(file)

                roll_col = df.columns[0]
                subject_cols = df.columns[1:]  # subject names

                for _, row in df.iterrows():
                    roll = str(row[roll_col]).strip()
                    try:
                        student = Student.objects.get(roll_number=roll)
                    except Student.DoesNotExist:
                        messages.warning(request, f"Student {roll} not found, skipping.")
                        continue

                    total_gp = Decimal("0.00")
                    count_gp = 0

                    for idx, subject_name in enumerate(subject_cols, start=1):
                        marks = row[subject_name]

                        if pd.isna(marks):
                            continue

                        try:
                            marks_decimal = Decimal(str(marks))
                        except InvalidOperation:
                            messages.error(request, f"Invalid marks for {roll} in {subject_name}, skipping.")
                            continue

                        grade_point = (marks_decimal / Decimal("10")).quantize(Decimal("0.01"))

                        # Update student semester subject names and grades
                        setattr(student, f"{sem}_sub{idx}_name", subject_name)
                        setattr(student, f"{sem}_sub{idx}_grade", grade_point)

                        total_gp += grade_point
                        count_gp += 1

                    # Calculate SGPA
                    sgpa_value = (total_gp / Decimal(count_gp)).quantize(Decimal("0.01")) if count_gp else None
                    setattr(student, f"sgpa{sem_num}", sgpa_value)

                    # Calculate CGPA as average of non-null SGPAs
                    sgpas = []
                    for i in range(1, 9):
                        sgpa_i = getattr(student, f"sgpa{i}", None)
                        if sgpa_i is not None:
                            sgpas.append(sgpa_i)
                    student.cgpa = (sum(sgpas) / Decimal(len(sgpas))).quantize(Decimal("0.01")) if sgpas else None

                    student.save()

                messages.success(request, f"Results for {sem} uploaded successfully!")
                return redirect("upload_results")

            except Exception as e:
                messages.error(request, f"Error processing file: {e}")

    else:
        form = UploadFileForm()

    return render(request, "upload_results.html", {"form": form})

def results(request):
    student = None
    semester_results = []
    sgpa_value = None
    cgpa_value = None
    sem = None

    if request.method == "POST":
        roll = request.POST.get("roll_number", "").strip()
        sem = request.POST.get("semester")
        
        if not sem or not sem.isdigit() or int(sem) not in range(1, 9):
            messages.error(request, "Please select a valid semester (1-8).")
        else:
            sem = int(sem)
            try:
                student = Student.objects.get(roll_number=roll)
                
                # Collect subject names and grades for the selected semester
                for i in range(1, 9):  # up to 8 subjects per semester
                    sub_name = getattr(student, f"sem{sem}_sub{i}_name", None)
                    grade = getattr(student, f"sem{sem}_sub{i}_grade", None)
                    if sub_name:  # only include if a subject exists
                        semester_results.append({
                            "subject": sub_name,
                            "grade": grade
                        })
                
                # Get SGPA and CGPA
                sgpa_value = getattr(student, f"sgpa{sem}", None)
                cgpa_value = student.cgpa

            except Student.DoesNotExist:
                messages.error(request, f"No student found with roll number {roll}")

    return render(request, "check_result.html",{
    "student": student,
    "semester_results": semester_results,
    "sgpa": sgpa_value,
    "cgpa": cgpa_value,
    "sem": sem,
    "semesters": range(1, 9),  # add this
})

