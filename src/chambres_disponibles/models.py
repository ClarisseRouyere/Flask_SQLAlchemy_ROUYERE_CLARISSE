from .database import db
from datetime import datetime

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    reservation = db.relationship('Reservation', backref='auteur', lazy='dynamic')

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    number =  db.Column(db.Integer)
    price =  db.Column(db.Integer)
    reservation = db.relationship('Reservation', backref='auteur', lazy='dynamic')
    
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    statut = db.Column(db.Text, nullable=False)
    date_arrived = db.Column(db.DateTime, default=datetime.utcnow)
    date_left = db.Column(db.DateTime, default=datetime.utcnow)
    id_client = db.Column(db.Integer, db.ForeignKey('Client.id')) 
    id_room = db.Column(db.Integer, db.ForeignKey('Room.id'))
