from django.shortcuts import render, HttpResponse

# Create your views here.
def get_resume(request):
    return render(
        request=request,
        template_name='resume/resume.html'
        )