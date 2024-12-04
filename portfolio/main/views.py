from django.shortcuts import render, get_object_or_404
from  .models import Project, Tag



def home(request): 
    return render(request, "home.html")

def portfolio(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "portfolio.html", {"projects": projects, "tags": tags})

def contact(request): 
    return render(request, "contact.html")

def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})
