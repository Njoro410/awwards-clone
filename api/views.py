from projects.models import Projects,Profile
from .serializers import ProfileSerializer,ProjectsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


#views here
@api_view
def GetProjects(request):
    projects = Projects.objects.all()
    serializer = ProjectsSerializer(projects, many = True)
    return Response(serializer.data)

@api_view
def GetProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)

@api_view
def GetSpecificProject(request,pk):
    article = Projects.objects.get(id=pk)
    serializer = ProfileSerializer(article, many = False)
    return Response(serializer.data)