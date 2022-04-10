from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profilepic = models.ImageField(
        upload_to='profile_pic/', default='Profile pic', blank=True)
    # projects = models.ForeignKey('Projects', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'


class Projects(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects/', default='https://wallpaperaccess.com/full/1129018.jpg')
    description = models.TextField()
    url = models.URLField()
    # rating = models.ForeignKey('Rating', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='rater')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    design = models.IntegerField(blank=True, null=True, default=0)
    usability = models.IntegerField(blank=True, null=True, default=0)
    content = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f'{self.project.title} Rating'
    
    
class Reviews(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviewer')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    review = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.review

