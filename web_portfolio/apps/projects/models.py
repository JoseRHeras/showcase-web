from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=40, blank=False)
    web_link = models.URLField(max_length=400, blank=False)

    def __str__(self):
        return f"{self.name}"