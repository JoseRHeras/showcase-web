from django.shortcuts import render
from personal_projects.models import Project


# Create your views here.
def project_list(request):
    projects = Project.objects.all()

    return render(request, 'personal_projects/project_list.html', {'projects' : projects})