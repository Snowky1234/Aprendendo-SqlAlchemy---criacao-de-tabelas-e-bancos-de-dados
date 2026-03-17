#importando as bibliotecas necessárias para criar o banco de dados e definir as tabelas
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

#criar o banco de dados e a sessão para interagir com ele
BancoDeDados = create_engine('sqlite:///banco_de_dados.db', echo=True)

Session = sessionmaker(bind=BancoDeDados)
session = Session()

#declarando a base para as tabelas do banco de dados
Base = declarative_base()

#TABELAS PAIS
class Artista(Base):
    __tablename__ = 'artista'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True)
    musica = relationship("Musica", back_populates="artista")  # Relacionamento para facilitar consultas

class Genero(Base):
    __tablename__ = 'genero'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True)
    musica = relationship("Musica", back_populates="genero")
    jogo = relationship("Jogo", back_populates="genero")

class Ritmo(Base):
    __tablename__ = 'ritmo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True)
    jogo = relationship("Jogo", back_populates="ritmo")  
    musica = relationship("Musica", back_populates="ritmo") 

class Plataforma(Base):
    __tablename__ = 'plataforma'
    id = Column(Integer, primary_key=True)
    plataforma = Column(String)
    jogo = relationship("Jogo", back_populates="plataforma")

#TABELAS FILHOS
class Musica(Base):
    __tablename__ = "Musica"
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String, nullable=False)
    
    # ForeignKeys CORRETOS (sempre apontando para .id)
    artista_id = Column(Integer, ForeignKey('artista.id'), nullable=False)
    genero_id  = Column(Integer, ForeignKey('genero.id'), nullable=False)
    ritmo_id   = Column(Integer, ForeignKey('ritmo.id'), nullable=False)

    #Relacionamentos para facilitar consultas
    artista = relationship("Artista", back_populates="musica")
    genero  = relationship("Genero", back_populates="musica")
    ritmo   = relationship("Ritmo", back_populates="musica")

class Jogo(Base):
    __tablename__ = "Jogo"
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String, nullable=False,)
    genero_id = Column(Integer, ForeignKey('genero.id'), nullable=False)
    ritmo_id = Column(Integer, ForeignKey('ritmo.id'), nullable=False)
    plataforma_id = Column(Integer, ForeignKey('plataforma.id'), nullable=False)

    genero = relationship("Genero", back_populates="jogo")  
    ritmo = relationship("Ritmo", back_populates="jogo")  
    plataforma = relationship("Plataforma", back_populates="jogo")  


Base.metadata.create_all(bind=BancoDeDados)
