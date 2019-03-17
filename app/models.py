from datetime import datetime
from app import sqlAlchemy_db, login
from flask_login import UserMixin

class User(UserMixin, sqlAlchemy_db.Model):
    userID = sqlAlchemy_db.Column(sqlAlchemy_db.Integer, primary_key=True)
    username = sqlAlchemy_db.Column(sqlAlchemy_db.String(64), index=True, unique=True)
    email = sqlAlchemy_db.Column(sqlAlchemy_db.String(120), index=True, unique=True)
    password = sqlAlchemy_db.Column(sqlAlchemy_db.String(128))
    firstName = sqlAlchemy_db.Column(sqlAlchemy_db.String(20))
    lastName = sqlAlchemy_db.Column(sqlAlchemy_db.String(20))
    role = sqlAlchemy_db.Column(sqlAlchemy_db.String(20))
    phoneNumber = sqlAlchemy_db.Column(sqlAlchemy_db.String(10))
    vehicles = sqlAlchemy_db.relationship('Vehicle', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Ticket(sqlAlchemy_db.Model):
    ticketID = sqlAlchemy_db.Column(sqlAlchemy_db.Integer, primary_key=True)
    vType = sqlAlchemy_db.Column(sqlAlchemy_db.String(20))
    description = sqlAlchemy_db.Column(sqlAlchemy_db.String(255))
    location = sqlAlchemy_db.Column(sqlAlchemy_db.String(50))
    amount = sqlAlchemy_db.Column(sqlAlchemy_db.Numeric(5,2))
    licensePlateNumber = sqlAlchemy_db.Column(sqlAlchemy_db.String(8))
    timestamp = sqlAlchemy_db.Column(sqlAlchemy_db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Ticket {}>'.format(self.vType)

class Vehicle(sqlAlchemy_db.Model):
    licensePlateNumber = sqlAlchemy_db.Column(sqlAlchemy_db.String(8), primary_key=True)
    model = sqlAlchemy_db.Column(sqlAlchemy_db.String(20))
    make = sqlAlchemy_db.Column(sqlAlchemy_db.String(20))
    userID = sqlAlchemy_db.Column(sqlAlchemy_db.Integer, sqlAlchemy_db.ForeignKey('user.userID'))

    def __repr__(self):
        return '<Vehicle {}>'.format(self.model)