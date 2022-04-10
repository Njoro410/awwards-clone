import profile
from django.contrib import admin
from .models import Profile,Projects,Rating,Reviews
# Register your models here.

admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Rating)
admin.site.register(Reviews)