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
    return render(request, 'about.html')

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)



def project(reqest):
    # projects = list(Project.objects.values());
    return render(reqest, 'projects.html')

def task(reqest):
    # task = get_object_or_404(Task, id=id)
    return render(reqest, 'tasks.html')