from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Sessao(Base):
    __tablename__ = 'sessoes'

    id = Column(Integer, primary_key=True)
    filme_id = Column(Integer, ForeignKey('filmes.id'), nullable=False)
    sala_id = Column(Integer, ForeignKey('salas.id'), nullable=False)
    horario = Column(DateTime, nullable=False)

    filme = relationship('Filme', back_populates='sessoes')
    sala = relationship('Sala', back_populates='sessoes')
    reservas = relationship('Reserva', back_populates='sessao')

    def json(self):
        return {
            'id': self.id,
            'filme_id': self.filme_id,
            'sala_id': self.sala_id,
            'horario': self.horario
        }
