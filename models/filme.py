from sqlalchemy import Column, Integer, String
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

    def json(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'duracao': self.duracao,
            'genero': self.genero,
            'estoque': self.estoque
        }
