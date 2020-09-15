# Importar a biblioteca de data e horario
from datetime import date, time, datetime, timedelta


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)

    # Formatação da data
    print('Data atual: '+data_atual.strftime('%d/%m/%Y'))

    # Dia da semana
    print('Dia da semana: '+data_atual.strftime('%A'))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario.strftime('%H:%M:%S'))
    print(type(horario_str))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print('Data e horário completo: '+data_atual.strftime('%d/%m/%Y'))
    print('Horário completo: '+data_atual.strftime('%H:%M:%S'))
    print('Data e horário completo em string: '+data_atual.strftime('%c'))
    print('Dia da semana: {}'.format(data_atual.weekday()))

    # Dias da semana traduzido
    tupla_dia = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    tupla_mes = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    print('Dia da semana traduzido: '+tupla_dia[data_atual.weekday()])
    print('Mês traduzido: '+tupla_mes[data_atual.month-1])

    # Criar data
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '10/01/2020 12:20:30'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print('Data convertida: {}'.format(data_convertida))
    print(type(data_convertida))

    # Contas com data usando timedelta
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=20)
    print(nova_data)


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()

