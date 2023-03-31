from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Classe modelo com os atributos do personagem.
class CharacterModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    image_link = db.Column(db.String(200), nullable=False)
    program = db.Column(db.String(50), nullable=False)
    animator = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Character(name={name},description={description},\
            image_link={image_link},program={program},animator={animator})"


# Método para criar a database
db.create_all()
"""
Aviso: 'db.create_all()' só é executado uma vez quando rodar o script pela primeira vez,
porque se não, uma nova database é criada, e ela é sobreposta sobre a anterior.
Por favor, deletar ou comentar 'db.create_all()' após executar 'main.py'.
"""

# Controlador dos argumentos para o método put
character_put_args = reqparse.RequestParser()
character_put_args.add_argument("name", type=str, help="name", required=True)
character_put_args.add_argument("description", type=str, help="description", required=True)
character_put_args.add_argument("image_link", type=str, help="image_link", required=True)
character_put_args.add_argument("program", type=str, help="program", required=True)
character_put_args.add_argument("animator", type=str, help="animador", required=True)

# Controlador dos argumentos para o método patch
character_update_args = reqparse.RequestParser()
character_update_args.add_argument("name", type=str)
character_update_args.add_argument("description", type=str)
character_update_args.add_argument("image_link", type=str)
character_update_args.add_argument("program", type=str)
character_update_args.add_argument("animator", type=str)

# Define como o objeto deve ser serializado.
resource_fields = {
    'id': fields.String,
    'name': fields.String,
    'description': fields.String,
    'image_link': fields.String,
    'program': fields.String,
    'animator': fields.String,
}


# Classe que contém os métodos request. 
class Character(Resource):
    @marshal_with(resource_fields)
    def get(self, char_id):
        # Define 'result' como o id do personagem requisitado.
        result = CharacterModel.query.filter_by(id=char_id).first()
        # Caso result seja inválido, aborte a operação.

        if not result:
            # HTTP response status code 404: não encontrado.
            abort(404, message="Não foi possível encontra um personagem nesse id.")
        # Caso seja válido, retorne as informações do id.
        return result

    @marshal_with(resource_fields)
    def put(self, char_id):
        # Variável com o método que analisa os argumentos passados.
        args = character_put_args.parse_args()
        # Define a variável 'result' como o id do personagem requisitado.
        result = CharacterModel.query.filter_by(id=char_id).first()
        # Caso result já exista, aborte e retorne uma mensagem de aviso.

        if result:
            # HTTP response status code 409: conflito.
            abort(409, message="Id do personagem já está em uso.")
        # Caso não exista, define-se os parâmetros a serem passados.
        put_char = CharacterModel(id=char_id,name=args['name'], description=args['description'],
                                   image_link=args['image_link'], program=args['program'], animator=args['animator'])
        # E adiciona o novo personagem na database.
        db.session.add(put_char)
        db.session.commit()

        # HTTP response status code 201: criado.
        return put_char, 201

    @marshal_with(resource_fields)
    def patch(self, char_id):
        # Variável com o método que analisa os argumentos passados.
        args = character_update_args.parse_args()
        # Define a variável 'result' como o id do personagem requisitado.
        result = CharacterModel.query.filter_by(id=char_id).first()
        # Caso result não exista, aborte a operação e retorne uma mensagem.

        if not result:
            # HTTP response status code 404: não encontrado.
            abort(404, message="Personagem não existe, logo não pode ser atualizado.")
        # Atualizando as informações com os argumentos passados.
        """
        Cada argumento é verificado separadamente,
        pois o usuário pode querer atualizar somente um dos argumentos.
        """
        if args['name']:
            result.name = args['name']
        if args['description']:
            result.description = args['description']
        if args['image_link']:
            result.image_link = args['image_link']
        if args['program']:
            result.program = args['program']
        if args['animator']:
            result.animator = args['animator']
        db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self, char_id):
            # Remove o personagem da database de acordo com o id passado.
            CharacterModel.query.filter_by(id=char_id).delete()
            db.session.commit()
            # HTTP response status code 204: sem conteúdo.
            return f'Sem conteúdo', 204


api.add_resource(Character, "/characters/<int:char_id>")

if __name__ == "__main__":
    app.run(debug=True)