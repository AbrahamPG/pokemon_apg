from django.contrib import admin
from .models import Owner

# Register your models here.
#admin.site.register(Owner)
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("nombre","pais","edad")
    list_filter = ("edad","pais")
    search_fields = ("nombre",)



#lo que se hace en el admin sobreescribe lo que se
#ponga en models
#list_display: muestra em pantalla en una tupla
#list_filter: creamos un filtrador
#fields=("edad",)    editar para cuando se pida agregar