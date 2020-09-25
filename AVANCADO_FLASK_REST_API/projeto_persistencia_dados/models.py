from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# Criar uma sessão
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
# Importar a base declarativa default
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///dev.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


# Criando a tabela
class Programadores(Base):
    # Renomeando o nome da tabela para programadores
    __tablename__ = 'programadores'

    id = Column(Integer, primary_key=True)
    # Index=True para criar um indice e deixar a consulta mais rapida
    nome = Column(String(50), index=True)
    idade = Column(Integer)
    email = Column(String(50))

    # __repr__ = Representação, imprime a lista dos objetos, função de consulta
    def __repr__(self):
        return '\nId: {}\nNome: {}\nIdade: {}\nE-mail: {}\n'.format(self.id, self.nome, self.idade, self.email)

    # Função para salvar o objeto
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para deletar o objeto
    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Criando a tabela
class Habilidades(Base):
    # Renomeando o nome da tabela para pessoas
    __tablename__ = 'habilidades'

    id = Column(Integer, primary_key=True)
    # Index=True para criar um indice e deixar a consulta mais rapida
    nome = Column(String(40), index=True)

    # __repr__ = Representação, imprime a lista dos objetos, função de consulta
    def __repr__(self):
        return '\nId: {}\nNome: {}'.format(self.id, self.nome)

    # Função para salvar o objeto
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para deletar o objeto
    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Criando a tabela
class Programadores_Habilidades(Base):
    # Renomeando o nome da tabela para pessoas
    __tablename__ = 'programadores_habilidades'

    id = Column(Integer, primary_key=True)

    # Criar o relacionamento entre as tabelas
    programador_id = Column(Integer, ForeignKey('programadores.id'))
    programador = relationship("Programadores")

    # Criar o relacionamento entre as tabelas
    habilidades_id = Column(Integer, ForeignKey('habilidades.id'))
    habilidade = relationship("Habilidades")

    # __repr__ = Representação, imprime a lista dos objetos, função de consulta
    def __repr__(self):
        return '\nDados: Nome: {}'.format(self.nome)

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