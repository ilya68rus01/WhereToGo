import json

from flask import jsonify


class Place(json.JSONEncoder):
    def __init__(self, **kwargs):
        super(Place, self).__init__(**kwargs)

    def set_fields(self, id, name, address, description, rate, img_src):
        self.id = id
        self.name = str(name)
        self.address = str(address)
        self.description = str(description)
        self.rate = int(rate)
        self.img_src = str(img_src)

    def get_place_as_json(self):
        return jsonify(id=self.id,
                       name=self.name,
                       address=self.address,
                       description=self.description,
                       rate=self.rate,
                       img_src=self.img_src)

    def default(self, object):
        if isinstance(object, Place):
            return {
                "place_id": object.id,
                "name": object.name,
                "address": object.address,
                "description": object.description,
                "rate": object.rate,
                "img_src": object.img_src
                }
        return {'__{}__'.format(object.__class__.__name__): object.__dict__}
