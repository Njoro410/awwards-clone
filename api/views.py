from projects.models import Projects,Profile
from .serializers import ProfileSerializer,ProjectsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


#views here
def getProjects(request):
    projects = Projects.objects.all()
    serializer = ProjectsSerializer(projects, many = True)
    return Response(serializer.data)
