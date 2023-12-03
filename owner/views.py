from django.shortcuts import render
#from . import views
# Create your views here.

#urlpatterns = [
#    path('owner_list/', views.owner_list, name = 'owner_list')
#]

def owner_list(request):

    data_context = {
        'nombre': 'katty Paredes',
        'edad': 20,
        'dni': '74096065',
        'pais': 'peru',
        'vigente': False,
    }

    return render(request, 'owner_list.html', context={'data': data_context})