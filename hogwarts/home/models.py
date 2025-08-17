from django.db import models
from multiselectfield import MultiSelectField

class Faculty(models.Model):

    ROLE_CHOICES = [
        ('Headmaster', 'Headmaster'),
        ('Dy Headmistress', 'Dy Headmistress'),
        ('Registrar', 'Registrar'),
        ('Dean-Placements', 'Dean-Placements'),
        ('Dean-Research & Development', 'Dean-Research & Development'),
        ('Dean-Academics', 'Dean-Academics'),
        ('Dean-Administration', 'Dean-Administration'),
        ('Acad. Associate Dean-Student Affairs', 'Acad. Associate Dean-Student Affairs'),
        ('Admin. Associate Dean-Faculty Affairs', 'Admin. Associate Dean-Faculty Affairs'),
        ('Acad. Associate Dean-Curriculum', 'Acad. Associate Dean-Curriculum'),
        ('Admin. Associate Dean-Magic and Safety', 'Admin. Associate Dean-Magic and Safety'),
        ('Controller of Examinations', 'Controller of Examinations'),
        ('Deputy Registrar', 'Deputy Registrar'),
        ('Assistant Controller of Examinations', 'Assistant Controller of Examinations'),
        ('HoD', 'HoD'),
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Visiting Faculty', 'Visiting Faculty'),
        ('Lecturer', 'Lecturer'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    experience_years = models.PositiveIntegerField(help_text="Total teaching/research experience in years")
    photo = models.ImageField(upload_to='faculty_photos/', blank=True, null=True)

    specialization = models.CharField(max_length=200, help_text="E.g. Potions, Charms, Defense Against the Dark Arts")

    roles = MultiSelectField(choices=ROLE_CHOICES, max_length=200, default=[], blank=True)
    other_roles = models.CharField(max_length=200, blank=True, help_text="Additional responsibilities, e.g. House Head, Quidditch Coach")

    bio = models.TextField()
    contact_email = models.EmailField(blank=True)
    office_location = models.CharField(max_length=100, blank=True)
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        roles_display = ", ".join(self.roles) if self.roles else "No Role"
        return f"{self.name} ({roles_display})"




from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    HOUSE_CHOICES = [
        ('GR', 'Gryffindor'),
        ('SL', 'Slytherin'),
        ('RB', 'Ravenclaw'),
        ('HB', 'Hufflepuff'),
    ]

    BLOOD_STATUS_CHOICES = [
        ('PB', 'Pureblood'),
        ('HB', 'Half-blood'),
        ('MB', 'Muggle-born'),
    ]

    full_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    house = models.CharField(max_length=2, choices=HOUSE_CHOICES)
    year = models.PositiveIntegerField(default=1)
    blood_status = models.CharField(max_length=2, choices=BLOOD_STATUS_CHOICES, default='MB')
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    joined_on = models.DateField(auto_now_add=True)

    # Subjects and grades for 8 semesters, 8 subjects each
    sem1_sub1_name = models.CharField(max_length=100, blank=True, null=True)
    sem1_sub1_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem1_sub2_name = models.CharField(max_length=100, blank=True, null=True)
    sem1_sub2_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem1_sub3_name = models.CharField(max_length=100, blank=True, null=True)
    sem1_sub3_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem1_sub4_name = models.CharField(max_length=100, blank=True, null=True)
    sem1_sub4_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem1_sub5_name = models.CharField(max_length=100, blank=True, null=True)
    sem1_sub5_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem1_sub6_name = models.CharField(max_length=100, blank=True, null=True)
    sem1_sub6_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem1_sub7_name = models.CharField(max_length=100, blank=True, null=True)
    sem1_sub7_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem1_sub8_name = models.CharField(max_length=100, blank=True, null=True)
    sem1_sub8_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # Repeat same pattern for semesters 2-8
    sem2_sub1_name = models.CharField(max_length=100, blank=True, null=True)
    sem2_sub1_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem2_sub2_name = models.CharField(max_length=100, blank=True, null=True)
    sem2_sub2_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem2_sub3_name = models.CharField(max_length=100, blank=True, null=True)
    sem2_sub3_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem2_sub4_name = models.CharField(max_length=100, blank=True, null=True)
    sem2_sub4_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem2_sub5_name = models.CharField(max_length=100, blank=True, null=True)
    sem2_sub5_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem2_sub6_name = models.CharField(max_length=100, blank=True, null=True)
    sem2_sub6_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem2_sub7_name = models.CharField(max_length=100, blank=True, null=True)
    sem2_sub7_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem2_sub8_name = models.CharField(max_length=100, blank=True, null=True)
    sem2_sub8_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # Semester 3
    sem3_sub1_name = models.CharField(max_length=100, blank=True, null=True)
    sem3_sub1_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem3_sub2_name = models.CharField(max_length=100, blank=True, null=True)
    sem3_sub2_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem3_sub3_name = models.CharField(max_length=100, blank=True, null=True)
    sem3_sub3_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem3_sub4_name = models.CharField(max_length=100, blank=True, null=True)
    sem3_sub4_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem3_sub5_name = models.CharField(max_length=100, blank=True, null=True)
    sem3_sub5_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem3_sub6_name = models.CharField(max_length=100, blank=True, null=True)
    sem3_sub6_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem3_sub7_name = models.CharField(max_length=100, blank=True, null=True)
    sem3_sub7_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem3_sub8_name = models.CharField(max_length=100, blank=True, null=True)
    sem3_sub8_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # Semester 4
    sem4_sub1_name = models.CharField(max_length=100, blank=True, null=True)
    sem4_sub1_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem4_sub2_name = models.CharField(max_length=100, blank=True, null=True)
    sem4_sub2_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem4_sub3_name = models.CharField(max_length=100, blank=True, null=True)
    sem4_sub3_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem4_sub4_name = models.CharField(max_length=100, blank=True, null=True)
    sem4_sub4_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem4_sub5_name = models.CharField(max_length=100, blank=True, null=True)
    sem4_sub5_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem4_sub6_name = models.CharField(max_length=100, blank=True, null=True)
    sem4_sub6_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem4_sub7_name = models.CharField(max_length=100, blank=True, null=True)
    sem4_sub7_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem4_sub8_name = models.CharField(max_length=100, blank=True, null=True)
    sem4_sub8_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # Semester 5
    sem5_sub1_name = models.CharField(max_length=100, blank=True, null=True)
    sem5_sub1_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem5_sub2_name = models.CharField(max_length=100, blank=True, null=True)
    sem5_sub2_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem5_sub3_name = models.CharField(max_length=100, blank=True, null=True)
    sem5_sub3_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem5_sub4_name = models.CharField(max_length=100, blank=True, null=True)
    sem5_sub4_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem5_sub5_name = models.CharField(max_length=100, blank=True, null=True)
    sem5_sub5_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem5_sub6_name = models.CharField(max_length=100, blank=True, null=True)
    sem5_sub6_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem5_sub7_name = models.CharField(max_length=100, blank=True, null=True)
    sem5_sub7_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem5_sub8_name = models.CharField(max_length=100, blank=True, null=True)
    sem5_sub8_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # Semester 6
    sem6_sub1_name = models.CharField(max_length=100, blank=True, null=True)
    sem6_sub1_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem6_sub2_name = models.CharField(max_length=100, blank=True, null=True)
    sem6_sub2_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem6_sub3_name = models.CharField(max_length=100, blank=True, null=True)
    sem6_sub3_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem6_sub4_name = models.CharField(max_length=100, blank=True, null=True)
    sem6_sub4_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem6_sub5_name = models.CharField(max_length=100, blank=True, null=True)
    sem6_sub5_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem6_sub6_name = models.CharField(max_length=100, blank=True, null=True)
    sem6_sub6_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem6_sub7_name = models.CharField(max_length=100, blank=True, null=True)
    sem6_sub7_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem6_sub8_name = models.CharField(max_length=100, blank=True, null=True)
    sem6_sub8_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # Semester 7
    sem7_sub1_name = models.CharField(max_length=100, blank=True, null=True)
    sem7_sub1_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem7_sub2_name = models.CharField(max_length=100, blank=True, null=True)
    sem7_sub2_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem7_sub3_name = models.CharField(max_length=100, blank=True, null=True)
    sem7_sub3_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem7_sub4_name = models.CharField(max_length=100, blank=True, null=True)
    sem7_sub4_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem7_sub5_name = models.CharField(max_length=100, blank=True, null=True)
    sem7_sub5_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem7_sub6_name = models.CharField(max_length=100, blank=True, null=True)
    sem7_sub6_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem7_sub7_name = models.CharField(max_length=100, blank=True, null=True)
    sem7_sub7_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem7_sub8_name = models.CharField(max_length=100, blank=True, null=True)
    sem7_sub8_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # Semester 8
    sem8_sub1_name = models.CharField(max_length=100, blank=True, null=True)
    sem8_sub1_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem8_sub2_name = models.CharField(max_length=100, blank=True, null=True)
    sem8_sub2_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem8_sub3_name = models.CharField(max_length=100, blank=True, null=True)
    sem8_sub3_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem8_sub4_name = models.CharField(max_length=100, blank=True, null=True)
    sem8_sub4_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem8_sub5_name = models.CharField(max_length=100, blank=True, null=True)
    sem8_sub5_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem8_sub6_name = models.CharField(max_length=100, blank=True, null=True)
    sem8_sub6_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem8_sub7_name = models.CharField(max_length=100, blank=True, null=True)
    sem8_sub7_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sem8_sub8_name = models.CharField(max_length=100, blank=True, null=True)
    sem8_sub8_grade = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # SGPA fields
    sgpa1 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sgpa2 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sgpa3 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sgpa4 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sgpa5 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sgpa6 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sgpa7 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sgpa8 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # Final CGPA
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.roll_number})"

    # Methods to calculate SGPA and CGPA
    def calculate_sgpa(self, semester):
        grades = []
        for i in range(1, 9):
            grade = getattr(self, f'sem{semester}_sub{i}_grade', None)
            if grade is not None:
                grades.append(grade)
        return round(sum(grades)/len(grades), 2) if grades else None

    def calculate_cgpa(self):
        sgpas = []
        for i in range(1, 9):
            sgpa = getattr(self, f'sgpa{i}', None)
            if sgpa is not None:
                sgpas.append(sgpa)
        return round(sum(sgpas)/len(sgpas), 2) if sgpas else None

    def update_grades(self):
        for i in range(1, 9):
            setattr(self, f'sgpa{i}', self.calculate_sgpa(i))
        self.cgpa = self.calculate_cgpa()
        self.save()

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    credits = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (Sem {self.semester}) - {self.code}"



class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    grade_point = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student.roll_number} - {self.subject.name} : {self.marks}"
