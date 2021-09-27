from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Profile

# Create your views here.
def home(request):
    user = Profile.objects.all()[0]
    return render(request, "landing_page/home.html", {'user' : user })