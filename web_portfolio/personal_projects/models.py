from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(default="Project", blank=False, max_length=50)
    link = models.CharField(default="Github Link",blank=False, max_length=200)

    def __str__(self):
        return self.name