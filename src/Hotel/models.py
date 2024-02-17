from .database import db
from datetime import datetime

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    reservations = db.relationship('Reservation', backref='client', lazy='dynamic')

class Chambre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    numero =  db.Column(db.Integer, unique=True, nullable=False)
    prix =  db.Column(db.Float, nullable=False)
    reservations = db.relationship('Reservation', backref='chambre', lazy='dynamic')
    
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    statut = db.Column(db.String(80), nullable=False)
    date_arrivee = db.Column(db.Date, nullable=False)
    date_depart = db.Column(db.Date, nullable=False)
    id_client = db.Column(db.Integer, db.ForeignKey('client.id')) 
    id_chambre = db.Column(db.Integer, db.ForeignKey('chambre.id'))
