from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, login, password):
        self.login = login
        self.password = password
