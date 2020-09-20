from django.contrib import admin
from core.models import Evento
# Register your models here.

# Definir o que aparecerá na lista de eventos
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    # Criar um filtro nessa visualização
    list_filter = ('usuario','titulo',)


admin.site.register(Evento, EventoAdmin)