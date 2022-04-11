from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Projects, Rating, Reviews,Profile
from .forms import ProjectsForm, ReviewForm
from django.views import View
import requests
from django.contrib.auth.decorators import login_required
# Create your views here.


def Index(request):
    # projects = getprojects()
    response = requests.get('https://awwards5652.herokuapp.com/api/allprojects/')

    projects = response.json()

    return render(request, 'index.html', {'projects': projects})

@login_required
def addProject(request):
    form = ProjectsForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        # form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return HttpResponseRedirect('/')
    return render(request, 'addProject.html', {'form': form})


def projectDetails(request, id):
    project = Projects.objects.get(id=id)
    response = requests.get(
        'https://awwards5652.herokuapp.com/api/specificProject/{}/'.format(id))
    # convert reponse data into json
    details = response.json()
    rating = Rating.objects.filter(project_id=id)
    reviews = Reviews.objects.filter(project_id=id)
    total = 0
    for i in rating:

        total += (i.usability + i.design + i.content)/3
        # t = float("{:.1f}".format(total))
    # print(total)

    return render(request, 'projectdetails.html', {'details': details, 'rating': rating, 'total': total, 'reviews': reviews, 'project':project})

@login_required
def addreview(request, id):
    form = ReviewForm(request.POST or None)
    if request.method == 'POST':
        # form = ProjectsForm(request.POST, request.FILES)
        content = request.POST['content']
        usability = request.POST['usability']
        design = request.POST['design']
        user = request.user
        project_id = id
        Rating.objects.create(content=content, design=design,
                              usability=usability, user=user, project_id=project_id)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.project_id = id
            data = review.save()

            return redirect('projectdetails',id)

    return render(request, 'addreview.html', {'form': form})

@login_required
def uProfile(request,id):
    response = requests.get('https://awwards5652.herokuapp.com/api/userDetails/{}/'.format(id))
    details = response.json()
    response2 = requests.get('https://awwards5652.herokuapp.com/api/userProjects/{}/'.format(id))
    projects = response2.json()
    response3 = requests.get('https://awwards5652.herokuapp.com/api/profile/{}/'.format(id))
    data = response3.json()
    user = request.user

    
    
    return render(request, 'profile.html', {'details':details,'projects': projects,'user': user,'data':data} )


def Search(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        projects = Projects.objects.filter(title=search_term)
        
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": projects})

    else:
        message = "You haven't searched for any project"
        return render(request, 'search.html', {"message": message})