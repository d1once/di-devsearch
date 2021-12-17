from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def kot_view(request):
    message = 'GTFO MUDA FUCKA!!!!'
    number = 5
    context = {"kot": "GTFO", 'number': number}
    return render(request, 'projects/kot.html', context)
