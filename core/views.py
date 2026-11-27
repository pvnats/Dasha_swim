from django.shortcuts import render

from core.models import Swimmer, Training


def home(request):
    return render(request, template_name='core/home.html')


def swimmer_list(request):
    swimmer_list = Swimmer.objects.all()
    return render(request, template_name='core/swimmer_list.html', context={'swimmer_list': swimmer_list})


def swimmer_details(request, swimmer_id):
    swimmer = Swimmer.objects.get(id=swimmer_id)
    return render(request, template_name='core/swimmer_details.html', context={'swimmer': swimmer})

def training_list(request):
    training_list = Training.objects.all()
    return render(request, template_name='core/training_list.html', context={'object_list': training_list})
