from django.urls import path
from personal_projects import views

urlpatterns = [
    path("", views.project_list, name="project_page")
]
