from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# Criar uma sessão
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
# Importar a base declarativa default
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

# Criando a tabela
class Pessoas(Base):
    # Renomeando o nome da tabela para pessoas
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    # Index=True para criar um indice e deixar a consulta mais rapida
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    # __repr__ = Representação, imprime a lista dos objetos, função de consulta
    def __repr__(self):
        return '\n<Id: {}\nPessoa: {}\nIdade: {}>'.format(self.id, self.nome, self.idade)

    # Função para salvar o objeto
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para deletar o objeto
    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Criando a tabela
class Atividades(Base):
    # Renomeando o nome da tabela para pessoas
    __tablename__ = 'atividades'

    id = Column(Integer, primary_key=True)

    # Index=True para criar um indice e deixar a consulta mais rapida
    nome = Column(String(80))

    # Criar o relacionamento entre as tabelas
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    # __repr__ = Representação, imprime a lista dos objetos, função de consulta
    def __repr__(self):
        return '\n<Atividades: {}>'.format(self.id, self.nome)

    # Função para salvar o objeto
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para deletar o objeto
    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Tabela de Usuarios
class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))

    # __repr__ = Representação, imprime a lista dos objetos, função de consulta
    def __repr__(self):
        return 'Usuario: {} - Login: {} - Senha: {}'.format(self.id, self.login, self.senha)

    # Função para salvar o objeto
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para deletar o objeto
    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    # Criar o banco de dados
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()