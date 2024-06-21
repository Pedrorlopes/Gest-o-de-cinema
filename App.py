from flask import Flask
from flask_restful import Api
from config import Config
from views.cliente_view import ClienteResource, ClienteListResource
from views.filme_view import FilmeResource, FilmeListResource
from views.reserva_view import ReservaResource, ReservaListResource
from views.sala_view import SalaResource, SalaListResource
from views.sessao_view import SessaoResource, SessaoListResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    api = Api(app)

    # Endpoints
    api.add_resource(ClienteListResource, '/clientes')
    api.add_resource(ClienteResource, '/clientes/<int:id>')
    api.add_resource(FilmeListResource, '/filmes')
    api.add_resource(FilmeResource, '/filmes/<int:id>')
    api.add_resource(ReservaListResource, '/reservas')
    api.add_resource(ReservaResource, '/reservas/<int:id>')
    api.add_resource(SalaListResource, '/salas')
    api.add_resource(SalaResource, '/salas/<int:id>')
    api.add_resource(SessaoListResource, '/sessoes')
    api.add_resource(SessaoResource, '/sessoes/<int:id>')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
