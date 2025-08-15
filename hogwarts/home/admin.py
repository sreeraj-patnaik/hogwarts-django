from django.contrib import admin
from home.models import Faculty, Department

# Register your models here.
admin.site.register([Faculty, Department])