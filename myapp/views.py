from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.


def index(request):
    title = "Django!!!!!!!!!!!!!"
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = "Reymar"
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, jugador):
    return HttpResponse("<h2>Hello %s</h2>" % jugador)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'project.html', {
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(title=title)
    return render(request, 'task.html')
