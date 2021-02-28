from psycopg2 import connect
import psycopg2

from Model.Place import Place

database_name = "where_to_go"
database_user_name = "postgres"
database_user_pass = "123"


class Database:
    def __init__(self):
        self.connection = connect(database=database_name, user=database_user_name, password=database_user_pass)

    def get_place(self, place_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM place WHERE place_id=%s;", (place_id))
        place_list = list()
        row = cursor.fetchone()
        place = Place()
        place.set_fields(row[0], row[1], row[2], row[3], row[4], row[5])
        return place

    def get_all_place(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM place;")
        place_list = list()
        rows = cursor.fetchall()
        for row in rows:
            p = Place()
            p.set_fields(row[0], row[1], row[2], row[3], row[4], row[5])
            place_list.append(p)
        return place_list

    def get_favorite_places(self, person):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM place WHERE place_id IN (SELECT place_id FROM favorite_place WHERE person_id=%s)", (person.id))
        place_list = list()
        rows = cursor.fetchall()
        for row in rows:
            p = Place()
            p.set_fields(row[0], row[1], row[2], row[3], row[4], row[5])
            place_list.append(p)
        return place_list

    # TODO Реализовать методы регистрации нового пользователя, входа в систему, поставки оценки заведению
    def insert_person(self):
        pass

    def sign_in(self):
        pass

    def set_rate(self):
        pass