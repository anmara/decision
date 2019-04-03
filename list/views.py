from django.shortcuts import render
from .models import Applicant


def home(request):
    context = {
        'posts': Applicant.objects.all()
    }
    return render(request, 'list/home.html', context)


def about(request):
    return render(request, 'list/home2.html', {'title': 'about'})
