from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profilepic = models.ImageField(upload_to = 'profile_pic/', default = 'Profile pic', blank = True)
    projects = models.ForeignKey('Projects', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Projects(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'projects/', default = 'image')
    description = models.TextField()
    url = models.URLField()
    
    def __str__(self):
        return self.title