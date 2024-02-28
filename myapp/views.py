from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title = 'Django Course!!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    userName = 'Jymydev'
    return render(request, 'about.html', {
        'userName' : userName
    })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)



def project(reqest):
    # projects = list(Project.objects.values());
    projects = Project.objects.all()
    return render(reqest, 'projects.html', {
        'projects': projects
    })

def task(reqest):
    # task = get_object_or_404(Task, id=id)

    tasks = Task.objects.all()
    return render(reqest, 'tasks.html', {
        'tasks': tasks
    })