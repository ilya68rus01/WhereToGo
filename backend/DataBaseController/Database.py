from psycopg2 import connect

from Model.Person import Person
from Model.Place import Place

database_name = "where_to_go"
database_user_name = "postgres"
database_user_pass = "1"


class Database:
    def __init__(self):
        self.connection = connect(database=database_name, user=database_user_name, password=database_user_pass)

    def get_place(self, place_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM place WHERE place_id=%s;", (place_id))
        row = cursor.fetchone()
        place = Place()
        place.set_fields(name=row[1],
                         address=row[2],
                         description=row[3],
                         rate=row[4],
                         img_src=row[5],
                         id=row[0])
        return place

    def get_all_place(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM place;")
        place_list = list()
        rows = cursor.fetchall()
        for row in rows:
            place = Place()
            place.set_fields(name=row[1],
                             address=row[2],
                             description=row[3],
                             rate=row[4],
                             img_src=row[5],
                             id=row[0])
            place_list.append(place)
        return place_list

    def get_favorite_places(self, person):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM place WHERE place_id IN (SELECT place_id FROM favorite_place WHERE person_id=%s)",
                       (person.id))
        place_list = list()
        rows = cursor.fetchall()
        for row in rows:
            p = Place()
            p.set_fields(row[0], row[1], row[2], row[3], row[4], row[5])
            place_list.append(p)
        return place_list

    def getUserById(self, person_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM person WHERE person_id=%s", [person_id])
        row = cursor.fetchall()
        user = Person()
        user.set_fields(row[0][0], row[0][1], row[0][2], row[0][3], row[0][4], row[0][5])
        user.set_password_hash(row[0][6])
        return user

    def getUserByLogin(self, login):
        cursor = self.connection.cursor()
        print(login)
        cursor.execute("SELECT * FROM person WHERE login=%(str)s", {"str": login})
        row = cursor.fetchall()
        if len(row) == 0:
            return None
        user = Person()
        user.set_fields(row[0][0], row[0][1], row[0][2], row[0][3], row[0][4], row[0][5])
        user.set_password_hash(row[0][6])
        print(user.name + " " + user.login + " " + user.password_hash)
        return user

    def insert_person(self, person):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO person (name, surname, patronymic, bday, login, password) VALUES (%s, %s, %s, %s, %s, %s)",
            (person.name, person.surname, person.patronymic, person.bday, person.login, person.password_hash))
        self.connection.commit()
        cursor.close()
        return None

    def add_place(self, place):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO place (name, adress, description, rate, photo_src) VALUES (%s, %s, %s, %s, %s)",
            (place.name, place.address, place.description, place.rate, place.img_src))
        self.connection.commit()
        cursor.close()
        return None
