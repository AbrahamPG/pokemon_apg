from . import views
from django.urls import path

urlpatterns = [
    path('owner_list/', views.owner_list, name='owner_list')
]
