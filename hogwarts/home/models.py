from django.db import models

# Create your models here.
from django.db import models

from django.utils.text import slugify

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)  # clean URL name
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Faculty(models.Model):
    ROLE_CHOICES = [
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer'),
        ('Visiting Faculty', 'Visiting Faculty'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    experience_years = models.PositiveIntegerField(help_text="Total teaching/research experience in years")
    photo = models.ImageField(upload_to='faculty_photos/', blank=True, null=True)
    
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='faculty_members')
    specialization = models.CharField(max_length=200, help_text="E.g. Potions, Charms, Defense Against the Dark Arts")
    
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    other_roles = models.CharField(max_length=200, blank=True, help_text="Additional responsibilities, e.g. House Head, Quidditch Coach")
    
    bio = models.TextField()
    contact_email = models.EmailField(blank=True)
    office_location = models.CharField(max_length=100, blank=True)
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"
