from django.contrib import admin
from gestionPedidos.models import Cliente, Articulo, Pedido

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    # This is the list of fields that will be displayed in the admin page
    list_display = ("nombre", "direccion", "tlfno")

    # This is the list of fields that will be used to filter the results
    search_fields = ("nombre", "tlfno")


class ArticuloAdmin(admin.ModelAdmin):
    list_filter = ("seccion",) # This is a tuple, so it must have a comma at the end


class PedidoAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha", "entregado")
    list_filter = ("fecha",)
    date_hierarchy = "fecha" # This will show the date hierarchy in the admin page

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedido)