from django.shortcuts import render
from apps.projects.models import Project

# Create your views here.
def projects(request):
    return render(request=request,
                  template_name="projects/projects.html",
                  context={'projects': Project.objects.all()}
    )