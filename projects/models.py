from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to= "images/")
    description = models.TextField()
    url = models.URLField(blank = True)
    video = models.FileField(upload_to="videos/", null=True, blank=True, default=None)
    used_tech = models.CharField(max_length=300, default=None)
    git_url = models.URLField(blank=True, null=True)
    CATEGORY = (
        ("django", 'Django'),
        ("pygame", "Pygame"),
        ("unreal", 'Unreal Engine 4'),
        ("godot", "Godot"),
    )
    owner = models.CharField(max_length=10, choices=CATEGORY, default="django")

    def short_description(self):
        if len(self.description) > 110:
            return self.description[100] + "..."

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'images/')
 
    def __str__(self):
        return self.project.title


class Tool(models.Model):
    CATEGORY = (
        ("W", 'Web'),
        ("G", 'Game'),
    )
    category = models.CharField(max_length=1, choices=CATEGORY, default="W")
    title = models.CharField(max_length=60)
    desc = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.title
