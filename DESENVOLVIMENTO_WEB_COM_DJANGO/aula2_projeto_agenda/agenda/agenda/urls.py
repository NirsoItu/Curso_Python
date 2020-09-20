
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Lista Json dos eventos
    path('agenda/list/', views.json_lista_eventos),

    # Listar todos os eventos
    path('agenda/list_all/', views.lista_eventos),

    # Listar todos os eventos do usuário
    path('agenda/by_user/', views.lista_eventos_por_usuario),

    # Redirecionar a pagina caso não digite endereço correto
    # path('', views.index),
    path('', RedirectView.as_view(url='/agenda/by_user')),

    # Acessar a pagina login
    path('agenda/login/', views.login_user),

    # Fazer login após o submit do form
    path('agenda/login/submit', views.login_submit),

    # Fazer logout
    path('logout', views.logout_user),

    path('agenda/list/<int:id_usuario>/', views.json_lista_eventos),

    path('agenda/evento/', views.evento),

    path('agenda/evento/submit', views.create_evento_submit),

    # Deletar evento
    path('agenda/delete/<int:id_evento>/', views.delete_evento),


]
