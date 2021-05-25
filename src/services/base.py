# srs/services/base.py
from typing import List

from sqlalchemy.exc import IntegrityError

from src import db


class Base:
    """
    This class is used as parent class for services   -  controllers,
    that process data between db and view functions.

    Concrete services are created as classes inherited from class Base
    with specify of the db.model.
    """
    model = None

    @classmethod
    def create_obj(cls, data: dict):
        """ Create and return object of class db.model. """

        obj = cls.model(**data)
        return obj

    @classmethod
    def get_all(cls):
        """ Retrieves all the objects class db.model. """

        objects = db.session.query(cls.model).all()
        return objects

    @classmethod
    def get_all_uuids(cls) -> List:
        """ Retrieves all the uuids of objects of class db.model. """

        return list(map(lambda obj: obj.uuid, cls.get_all()))

    @classmethod
    def get_by_uuid(cls, uuid: str):
        """ Retrieves the object of class db.model by uuid. """
        obj = db.session.query(cls.model).filter_by(uuid=uuid).first()
        return obj

    @staticmethod
    def save_to_db(obj) -> None:
        """ Takes object of class db model and saves it to db """
        db.session.add(obj)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

    @staticmethod
    def delete_from_db(obj):
        """ Takes object of class db model and delete it from db """
        db.session.delete(obj)
        db.session.commit()
