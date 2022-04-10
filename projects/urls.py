from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.Index, name='home'),
    path('addproject/',views.addProject, name='addproject'),
    path('projectdetails/<str:id>/',views.projectDetails,name='projectdetails'),
    path('addreview/<str:id>',views.addreview,name='addreview'),
    path('profile/<str:id>/',views.uProfile,name="profile"),
    path('search/', views.Search, name='search_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)