from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage, Tool

def home(request):
    return render(request, "projects/home.html")

def detail_view(request, id):
    project = get_object_or_404(Project, id=id)
    photos = ProjectImage.objects.filter(project=project)
    return render(request, 'projects/detail.html', {
        'project':project,
        'photos':photos
    })

def web_development(request):
    tools = Tool.objects.filter(category="W")
    return render(request, "projects/web/web_dev.html", {"tools":tools})

def game_development(request):
    tools = Tool.objects.filter(category="G")
    return render(request, "projects/game/game_dev.html", {"tools":tools})

def gameprojects(request, name):
    projects = Project.objects.filter(owner=name)
    return render(request, "projects/game/gameprojects.html", {"projects":projects})

def webprojects(request, name):
    #project = get_object_or_404(Project, owner=name)
    projects = Project.objects.filter(owner=name)
    return render(request, "projects/web/webprojects.html", {"projects":projects})


