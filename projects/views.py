from django.shortcuts import render
from .models import Project
# Create your views here.


def kot_view(request):
    projects = Project.objects.all()
    message = 'GTFO MUDA FUCKA!!!!'
    number = 5
    context = {"kot": message, 'number': number, "projects": projects}
    return render(request, 'projects/kot.html', context)
