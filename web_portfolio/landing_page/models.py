from django.db import models
from PIL import Image

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(default="FirstName", blank=False, max_length=25)
    middle_name = models.CharField(default="", blank=True, max_length=25)
    last_name = models.CharField(default="LastName", blank=False, max_length=25)
    profile_image = models.ImageField(default="avatar.bmp", upload_to="profile_pics")

    short_message = models.TextField(max_length=110, blank=False)
    welcome_message = models.TextField(max_length=60, blank=False)
    paragraph_message = models.TextField(max_length=400, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} profile."

    #Resize saved profile image
    def save(self):
        super().save()
        img = Image.open(self.profile_image.path)

        if(img.height > 1300 or img.width > 1300):
            output_size = (1300, 1300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)


# Stores database links to outside sources such as github, etc
class SocialPlatforms(models.Model):
    name = models.CharField(default="PlatformName", blank=False, max_length=30)
    link = models.CharField(default="Social Link", blank=False, max_length=150)
    icon = models.CharField(default="fas fa-user-friends", blank=True, max_length=60)

    def __str__(self):
        return f"{self.name} Link"

