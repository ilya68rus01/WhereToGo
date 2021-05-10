import json

from flask import url_for
from flask_login import current_user, login_user, logout_user
from flask_restful import Resource, reqparse
from werkzeug.utils import redirect

from DataBaseController.Database import Database
from FlaskService import app, api, login
from Model.Person import Person
from Model.Place import Place


def start():
    global database_controller
    database_controller = Database()
    api.add_resource(Places, "/places")
    api.add_resource(ConcretePlace, '/places/<place_id>')
    api.add_resource(FavoritePlaces, "/favorite_places", "/favorite_places/")
    api.add_resource(Login, "/login")
    app.run(debug=True, host='0.0.0.0', port=8000)


@login.user_loader
def load_user(user_id):
    return database_controller.getUserById(int(user_id))


# Получение списка всех мест
class Places(Resource):
    # Метод для отправки всех мест в формате json
    def get(self):
        place_list = database_controller.get_all_place()
        return json.dumps(place_list, cls=Place)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('adress')
        parser.add_argument('description')
        parser.add_argument('rate')
        parser.add_argument('img_src')
        args = parser.parse_args()
        name = str(args['name'])
        adress = str(args['adress'])
        description = str(args['description'])
        rate = str(args['rate'])
        img_src = str(args['img_src'])
        place = Place()
        place.set_fields(id=None,
                         name=name,
                         address=adress,
                         description=description,
                         rate=rate,
                         img_src=img_src)
        database_controller.add_place(place)


# Получение конкретного места
class ConcretePlace(Resource):
    def get(self, place_id):
        place = database_controller.get_place(place_id)
        return json.dumps(place, cls=Place)


# Получение списка любимых мест человека
class FavoritePlaces(Resource):
    def get(self):
        person = current_user
        place_list = database_controller.get_favorite_places(person)
        # TODO На основе любимых мест нейронка генерирует совет куда сходить и отправляет список таких мест
        return json.dumps(place_list, cls=Place)


class Login(Resource):
    ## TODO если аноним то кинуть ему окно на регистрацию
    def get(self):
        if current_user.is_authenticated:
            return redirect('places')
        if current_user.is_anonymous:
            return redirect('login')
        return redirect('places')

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login')
        parser.add_argument('password')
        parser.add_argument('name')
        parser.add_argument('surname')
        parser.add_argument('patronymic')
        parser.add_argument('bday')
        args = parser.parse_args()
        login = str(args['login'])
        password = str(args['password'])
        name = str(args["name"])
        surname = str(args["surname"])
        patronymic = str(args["patronymic"])
        bday = str(args["bday"])
        user = database_controller.getUserByLogin(login)
        if user is None:
            user = Person()
            user.set_fields(None, name, surname, patronymic, bday, login)
            user.set_password(password)
            database_controller.insert_person(user)
            user = database_controller.getUserByLogin(login)
        login_user(user, remember=True)
        return json.dumps("Login success")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('places'))
