from datetime import date, datetime
from app import db,login_manager
from flask_login import UserMixin, current_user

class User (db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255),unique=True, nullable=False)
    image=db.Column(db.String(256))

    def __repr__(self):
        return f"User('{self.id}', '{self.login}', '{self.password}', '{self.email}', '{self.image}')"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Categorys (db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(256))
    category = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.image}', '{self.category}')"


class Product(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(256))
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    category = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"User('{self.id}', '{self.category}', '{self.name}', '{self.image}', '{self.description}', '{self.price}')"

# def is_authenticated(self):
#     return current_user.is_authenticated