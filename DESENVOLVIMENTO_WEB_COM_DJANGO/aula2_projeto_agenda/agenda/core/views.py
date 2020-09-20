from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

# Exercício buscar através de requisição.
# def eventos(request, titulo_evento):
#     return HttpResponse('Nome do Evento: {}'.format(Evento.objects.get(titulo = titulo_evento)))

# Função para chamar a página de login
def login_user(request):
    return render(request, 'login.html')

# Função de logout do sistema
def logout_user(request):
    logout(request)
    return redirect('/')

# Função login no sistema
def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido!")
    return redirect('/')

# Exigir autenticação do usuário
@login_required(login_url='/agenda/login/')

# Listar todos eventos
def lista_eventos(request):
    evento = Evento.objects.all
    eventos_all = {'eventos': evento}
    return render(request,'agenda.html', eventos_all)

# Listar todos eventos de um usuario especifico
def lista_eventos_por_usuario(request):
    usuario = request.user
    # Filtro por data e horario até uma hora antes do evento
    data_atual = datetime.now() - timedelta(hours=1)
    # Colocar o gt para acima da data
    evento = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual)
    eventos_all = {'eventos': evento}
    return render(request,'agenda.html', eventos_all)

# Lista o evento de acordo com o parametro informado (id)
def evento(request):
    id_evento = request.GET.get('id')
    print(id_evento)
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request,'evento.html', dados)

# Função para redirecionar a pagina caso não digite endereço correto
def index(request):
    return redirect(request,'/agenda/list_all')

# Função para criar evento
@login_required(login_url='/agenda/login/')
def create_evento(request):
    return render(request, 'evento.html')

# Função para criar evento
@login_required(login_url='/agenda/login/')
def create_evento_submit(request):
    # Função do Botão Salvar
    if request.POST:
        titulo = request.POST.get("titulo")
        data_evento = request.POST.get("data_evento")
        descricao = request.POST.get("descricao")
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        # Função do Botão Editar
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.save()
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)
    return redirect('/')

# Função para deletar evento
@login_required(login_url='/agenda/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    # Padronizar o possível erro
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

def json_lista_eventos(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values(
        'id','titulo','data_evento', 'descricao', 'data_criacao')
    return JsonResponse(list(evento), safe=False)
