from sqlalchemy import Table, ForeignKey
from sqlalchemy import (
    Integer, String, DateTime, Text)
from sqlalchemy.orm import column_property
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True, index=True)
    first_name = db.Column(String(64))
    last_name = db.Column(String(64))
    full_name = column_property(first_name + ' ' + last_name)
    email = db.Column(Text, unique=True, index=True)
    password_hash = db.Column(String(128))
    member_since = db.Column(DateTime, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: %r, name: %r>' \
                % (self.id, self.full_name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.full_name
        }
