import json
from flask import jsonify


class Person(json.JSONEncoder):
    def __init__(self, **kwargs):
        super(Person, self).__init__(**kwargs)

    def set_fields(self, id, name, surname, patronymic, bday):
        self.id = str(id)
        self.name = str(name)
        self.surname = str(surname)
        self.patronymic = str(patronymic)
        self.bday = str(bday)

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