from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to= "images/")
    description = models.TextField()
    url = models.URLField(blank = True)
    

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