from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

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

    def json(self):
        return {
            'id': self.id,
            'filme_id': self.filme_id,
            'cliente_id': self.cliente_id,
            'sessao_id': self.sessao_id,
            'nota_avaliacao': self.nota_avaliacao
        }
