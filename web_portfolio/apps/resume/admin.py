from django.contrib import admin
from apps.resume.models import *

# Register your models here.
admin.site.register(GenericInformation)
admin.site.register(ExternalLink)
admin.site.register(Skill)
admin.site.register(EducationalInstitution)