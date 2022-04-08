from django.urls import path
from . import views

urlpatterns = [
    path('allprojects/', views.GetProjects, name='allprojects'),
    path('profile/<str:pk>/',views.GetProfile,name='profile'),
    path('specific-project/<str:pk>/',views.GetSpecificProject,name = 'specific-project')
]
