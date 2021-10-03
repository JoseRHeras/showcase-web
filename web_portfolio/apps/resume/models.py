from django.db import models
# Create your models here.

class GenericInformation(models.Model):
    name = models.CharField(max_length=70, blank=False, default="User Name")
    objective = models.TextField()

    def __str__(self) -> str:
        return f"' {self.name} ' information."

class InformationItem(models.Model):
    owner = models.ForeignKey(GenericInformation, on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    icon = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class EducationalInstitution(models.Model):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=80)
    location = models.CharField(max_length=50)
    graduation_date = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"School name: {self.name}"

    
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



