from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Criar  tabela desejada
class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')

    # Permitir a criação de uma tabela de evento para cada usuário
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Exigir que a tabela se chame evento
    class Meta:
        db_table = 'evento'

    # Retorna o nome do evento na listagem da table
    def __str__(self):
        return self.titulo

    # Formatando a data do evento
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y - %H:%M hs')

    # Formatando a data para editar
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False

