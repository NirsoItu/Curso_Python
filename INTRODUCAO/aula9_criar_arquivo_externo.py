# Criar um arquivo txt
# Insira o nome do arquivo com sua extensão, 'w' para escrever (write)
# arquivo = open('teste.txt', 'w')
# arquivo.write('Minha primeira escrita no arquivo')
# arquivo.close()

# Atualizar um arquivo txt
# Insira o nome do arquivo com sua extensão, 'a' para escrever (write)
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nMinha segunda escrita no arquivo')
# arquivo.close()

#importar a biblioteca para copiar editar e excluir arquivos
import shutil

diretorio_criacao_arquivo = 'C:/Users/Rogerio/Desktop/'
diretorio_copiar_arquivo = 'C:/Users/Rogerio/Desktop/Nova'

def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(diretorio_criacao_arquivo+'/'+nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(diretorio_criacao_arquivo+'/'+nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(diretorio_criacao_arquivo+'/'+nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(diretorio_criacao_arquivo + '/' + nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        # Separar a lista pelas virgulas
        lista_notas = x.split(',')

        # Inicia o objeto aluno em 0
        aluno = lista_notas[0]

        # Excluir o primeiro elemento da lista
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)

        # Converte os elemento da lista em interios para fazer a media
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))

        # Inclui todos os resultados em um conjunto
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    # Inserir o local e arquivo que eu quero copiar e o endereco a ser copiado
    shutil.copy(diretorio_criacao_arquivo+'/'+nome_arquivo, diretorio_copiar_arquivo)

def mover_arquivo(nome_arquivo):
    # Inserir o local e arquivo que eu quero mover e o endereco a ser movido
    shutil.move(diretorio_criacao_arquivo+'/'+nome_arquivo, diretorio_copiar_arquivo)

if __name__ == '__main__':
    #escrever_arquivo('notas.txt','Primeira linha. \n')
    #atualizar_arquivo('notas.txt','Mais uma linha')
    #ler_arquivo(diretorio_arquivo)

    # notas_aluno = 'Aparecida, 8, 5, 6, 9\n'
    # #escrever_arquivo('notas.txt', notas_aluno)
    # #atualizar_arquivo('notas.txt', notas_aluno)
    # #ler_arquivo('notas.txt')
    # media_notas('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)

    #copia_arquivo('notas.txt')
    mover_arquivo('notas.txt')








