from django.contrib import admin
from .models import Catalog

# Register your models here.
#admin.site.register(Owner)
@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("nombre","pais","edad")
    list_filter = ("edad","pais")
    search_fields = ("nombre",)
