from projects.models import Projects,Profile,Rating
from .serializers import ProfileSerializer,ProjectsSerializer,RatingSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view


#views here
@api_view(['GET'])
def GetProjects(request):
    projects = Projects.objects.all()
    serializer = ProjectsSerializer(projects, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def GetUserDetails(request,pk):
    profile = User.objects.get(id=pk)
    serializer = UserSerializer(profile, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def GetProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def GetSpecificProject(request,id):
    article = Projects.objects.get(id=id)
    serializer = ProjectsSerializer(article, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def GetSpecificRating(request,pk):
    rating = Rating.objects.filter(project_id=pk)
    serializer = RatingSerializer(rating, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def GetUserProjects(request,pk):
    projects = Projects.objects.filter(owner_id=pk)
    serializer = ProjectsSerializer(projects, many = True)
    return Response(serializer.data)
