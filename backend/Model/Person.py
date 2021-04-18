import json

from flask import jsonify
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Person(UserMixin, json.JSONEncoder):
    def __init__(self,
                 name=None,
                 surname=None,
                 patronymic=None,
                 bday=None,
                 login=None,
                 **kwargs):
        super(Person, self).__init__(**kwargs)
        self.name = str(name)
        self.surname = str(surname)
        self.patronymic = str(patronymic)
        self.bday = str(bday)
        self.login = str(login)

    def set_fields(self, id, name, surname, patronymic, bday, login):
        self.id = str(id)
        self.name = str(name)
        self.surname = str(surname)
        self.patronymic = str(patronymic)
        self.bday = str(bday)
        self.login = str(login)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def set_password_hash(self, password):
        self.password_hash = password

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_person_as_json(self):
        return jsonify(id=self.id,
                       name=self.name,
                       surname=self.surname,
                       patronymic=self.patronymic,
                       bday=self.bday)

    def default(self, object):
        if isinstance(object, Person):
            return {
                "person_id": object.id,
                "name": object.name,
                "surname": object.surname,
                "patronymic": object.patronymic,
                "bday": object.bday
                }
        return {'__{}__'.format(object.__class__.__name__): object.__dict__}