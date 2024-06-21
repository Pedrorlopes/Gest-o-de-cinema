from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from . import Base

class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    duracao = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)
    estoque = Column(Integer, nullable=False)

    reservas = relationship('Reserva', back_populates='filme')
    sessoes = relationship('Sessao', back_populates='filme')


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)

    reservas = relationship('Reserva', back_populates='cliente')


class Reserva(Base):
    __tablename__ = 'reservas'

    id = Column(Integer, primary_key=True)
    filme_id = Column(Integer, ForeignKey('filmes.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    sessao_id = Column(Integer, ForeignKey('sessoes.id'), nullable=False)
    nota_avaliacao = Column(Float, nullable=False)

    filme = relationship('Filme', back_populates='reservas')
    cliente = relationship('Cliente', back_populates='reservas')
    sessao = relationship('Sessao', back_populates='reservas')


class Sala(Base):
    __tablename__ = 'salas'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    capacidade = Column(Integer, nullable=False)

    sessoes = relationship('Sessao', back_populates='sala')


class Sessao(Base):
    __tablename__ = 'sessoes'

    id = Column(Integer, primary_key=True)
    filme_id = Column(Integer, ForeignKey('filmes.id'), nullable=False)
    sala_id = Column(Integer, ForeignKey('salas.id'), nullable=False)
    horario = Column(DateTime, nullable=False)

    filme = relationship('Filme', back_populates='sessoes')
    sala = relationship('Sala', back_populates='sessoes')
    reservas = relationship('Reserva', back_populates='sessao')
