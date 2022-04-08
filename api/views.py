from projects.models import Projects,Profile
from .serializers import ProfileSerializer,ProjectsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


#views here
@api_view
def getProjects(request):
    projects = Projects.objects.all()
    serializer = ProjectsSerializer(projects, many = True)
    return Response(serializer.data)


def getProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)