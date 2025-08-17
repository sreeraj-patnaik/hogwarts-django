from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name='home'),
    path("faculty/", views.faculty_list, name="faculty_list"),  # faculty list, no dept_name
    path("admin/", admin.site.urls),
    path("upload-results/", views.upload_results, name="upload_results"),
        path("results/", views.results, name="results"),  # 👈 Add this


]