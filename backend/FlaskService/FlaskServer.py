import flask
from flask import jsonify
from DataBaseController.Database import Database
from FlaskService import app, api
from flask_restful import Resource, reqparse

from Model.Person import Person
from Model.Place import Place
import json


def start():
    global database_controller
    database_controller = Database()
    api.add_resource(Places, "/places")
    api.add_resource(ConcretePlace, '/places/<place_id>')
    api.add_resource(FavoritePlaces, "/favorite_places", "/favorite_places/")
    app.run(debug=True, host='0.0.0.0', port=8000)


# Получение списка всех мест
class Places(Resource):
    # def post(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('comment')
    #     parser.add_argument('text')
    #     args = parser.parse_args()
    #     comment = str(args['comment']).lower()
    #     text = str(args['text']).lower()
    #     return "Hello world", 200

    # Метод для отправки всех мест в формате json

    def get(self):
        place_list = database_controller.get_all_place()
        return json.dumps(place_list, cls=Place)


# Получение конкретного места
class ConcretePlace(Resource):
    def get(self, place_id):
        place = database_controller.get_place(place_id)
        return json.dumps(place, cls=Place)


# Получение списка любимых мест человека
class FavoritePlaces(Resource):
    def get(self):
        person = Person()
        person.set_fields(1, "Илья", "Хрущев", "Игоревич", "21.11.1998")
        place_list = database_controller.get_favorite_places(person)
        return json.dumps(place_list, cls=Place)