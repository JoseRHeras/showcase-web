from django.shortcuts import render
from apps.resume import models

# Create your views here.
def get_resume(request):
    general_info = models.GenericInformation.objects.all()[0]
    skills = models.Skill.objects.all()
    schools = models.EducationalInstitution.objects.all()

    return render(
        request=request,
        template_name='resume/resume.html',
        context= {
            "general" : general_info,
            "skills" : skills,
            "schools" : schools
            }   
        )