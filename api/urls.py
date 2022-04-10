from django.urls import path
from . import views

urlpatterns = [
    path('allprojects/', views.GetProjects, name='allprojects'),
    path('profile/<str:pk>/',views.GetProfile,name='profile'),
    path('userDetails/<str:pk>/',views.GetUserDetails,name='user'),
    path('specificProject/<str:id>/',views.GetSpecificProject,name = 'projectdetails'),
    path('rating/<str:pk>/',views.GetSpecificRating, name='projectrating'),
    path('userProjects/<str:pk>/',views.GetUserProjects, name='userprojects'),
]
