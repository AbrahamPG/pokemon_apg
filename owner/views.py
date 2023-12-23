from django.shortcuts import render
from . import views

def owner_list(request):
    data_context = [
        {
            'nombre': 'katty paredes',
            'edad': 16,
            'dni': '75085064',
            'pais': 'Peru',
            'vigente': False,
        },
        {
            'nombre': 'Mario Mejia',
            'edad': 18,
            'dni': '75256064',
            'pais': 'Peru',
            'vigente': False,
        },
        {
            'nombre': 'Benito Montes',
            'edad': 27,
            'dni': '75078964',
            'pais': 'Peru',
            'vigente': True,
        }
        ]
    return render(request, 'owner_list.html', context={'data': data_context})