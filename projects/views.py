from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage

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
    return render(request, "projects/web/web_dev.html")

def game_development(request):
    return render(request, "projects/game/game_dev.html")
