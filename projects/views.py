from django.shortcuts import render, redirect
from .models import Project
from .forms import KotForm
# Create your views here.


def kot_view(request):
    projects = Project.objects.all()
    message = 'GTFO MUDA FUCKA!!!!'
    number = 5
    context = {"kot": message, 'number': number, "projects": projects}
    return render(request, 'projects/kot.html', context)


def create_kot(request):
    form = KotForm()
    if request.method == 'POST':
        form = KotForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('kot')

    context = {'form': form}
    return render(request, 'projects/kot_form.html', context)


def update_kot(request, pk):
    project = Project.objects.get(id=pk)
    form = KotForm(instance=project)
    if request.method == 'POST':
        form = KotForm(request.POST, instance=project)
        if(form.is_valid()):
            form.save()
            return redirect('kot')

    context = {'form': form}
    return render(request, 'projects/kot_form.html', context)
