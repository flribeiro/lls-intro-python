from django.contrib import admin
from .models import Area, Plantonista


@admin.register(Plantonista)
class PlantonistaAdmin(admin.ModelAdmin):
    model = Plantonista
    list_display = ['id', 'área', 'nome', 'observação']
    list_editable = ['observação']
    list_filter = ['id', 'nome']
    search_fields = ['id', 'área', 'nome', 'observação']
    save_on_top = True


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    model = Area
    list_display = ['nome']
    search_fields = ['nome']
    save_on_top = True


# admin.site.register(Plantonista)
# admin.site.register(Area)
