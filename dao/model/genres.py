# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью
# (но не с базой, с базой мы работает в классе DAO)

# Пример

from setup_db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    movies = db.relationship('Movie', backref='genre_', lazy='dynamic')


# OPTION #1
from marshmallow import fields, Schema  # noqa


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


# OPTION #2
from pydantic import BaseModel  # noqa
from typing import Optional  # noqa


class GenreBM(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True
