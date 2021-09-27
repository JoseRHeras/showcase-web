from django.db import models
# Create your models here.

class GenericInformation(models.Model):
    name = models.CharField(max_length=70, blank=False, default="User Name")
    location = models.CharField(max_length=50, blank=False, default="Chicago")
    email = models.EmailField(max_length=254, blank=True)

    objective = models.TextField()

    def __str__(self) -> str:
        return f"' {self.name} ' information."

class EducationalInstitution(models.Model):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=80)
    location = models.CharField(max_length=50)
    graduation_date = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"School name: {self.name}"

class ExternalLink(models.Model):
    name = models.CharField(max_length=50, blank=False, default="Worded Icon Name")
    description = models.CharField(max_length=80, blank=True)
    url_link = models.URLField(max_length=200, blank=True)
    ft_awesome_name = models.CharField(max_length=70, blank=False, default="fas fa-atom")

    FIELD_CHOICES = [
        ('SOCIAL_MEDIA', 'Social Media'),
        ('GENERAL_DATA', 'General Data'),
        
    ]
    icon_type = models.CharField(max_length=50, blank=False, choices=FIELD_CHOICES, default='SOCIAL_MEDIA')

    def __str__(self) -> str:
        return f"Link for {self.name}"
    
class Skill(models.Model):
        name = models.CharField(max_length=50)
        icon = models.CharField(max_length=50, blank=False, default="fas fa-atom")
        SKILL_TYPE = [
        ('SOFT_SKILL', 'Soft skill'),
        ('TECHNICAL_SKILL', 'Technical Skill')    
        ]
        skill_type = models.CharField(max_length=50, choices=SKILL_TYPE, default='SOFT_SKILL', blank=False)

        def __str__(self) -> str:
            return f"{self.skill_type}: {self.name}"



