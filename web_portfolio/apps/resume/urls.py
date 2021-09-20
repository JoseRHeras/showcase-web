from django.urls import path
from apps.resume import views

urlpatterns = [
    path('', views.get_resume, name="personal_resume")
]