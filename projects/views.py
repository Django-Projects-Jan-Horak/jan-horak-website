from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, ProjectImage, Tool, Certificate
from django.core.mail import send_mail


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
    return render(request, "projects/game/gameprojects.html", {"projects":projects, "name":name})

def webprojects(request, name):
    #project = get_object_or_404(Project, owner=name)
    projects = Project.objects.filter(owner=name)
    return render(request, "projects/web/webprojects.html", {"projects":projects, "name":name})

def detail_game(request, id):
    project = get_object_or_404(Project, id=id)
    photos = ProjectImage.objects.filter(project=project)
    return render(request, 'projects/game/detail_game.html', {
        'project':project,
        'photos':photos
    })

def detail_web(request, id):
    project = get_object_or_404(Project, id=id)
    photos = ProjectImage.objects.filter(project=project)
    return render(request, 'projects/web/detail_web.html', {
        'project':project,
        'photos':photos
    })
def about_me(request):
    return render(request, 'projects/about_me.html')
    
def certificates(request):
    webs = Certificate.objects.filter(category="W")
    games = Certificate.objects.filter(category="G")
    return render(request, 'projects/certificates.html', {"webs":webs, "games":games})

def email(request):
    return render(request, "projects/email.html", {"message":""})

def send_email(request):
    if request.method == "POST":
        send_mail(
            request.POST["subject"],
            request.POST["message"],
            request.POST["from_mail"],
            ['janhorak58@gmail.com'],
        )
    
        return redirect("send_email")

    else:
        return render(request, "projects/email.html", {"message":"Email Successfully sent"})



