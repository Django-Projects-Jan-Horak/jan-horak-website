from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage


def home(request):
    projects = Project.objects.all()
    return render(request, "projects/home.html", {"projects":projects})

def detail_view(request, id):
    project = get_object_or_404(Project, id=id)
    photos = ProjectImage.objects.filter(project=project)
    return render(request, 'projects/detail.html', {
        'project':project,
        'photos':photos
    })