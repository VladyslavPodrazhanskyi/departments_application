from src import db


class Base:
    model = None

    @classmethod
    def create_obj(cls, data):
        obj = cls.model(**data)
        return obj

    @classmethod
    def get_all(cls):
        objects = db.session.query(cls.model).all()
        return objects

    @classmethod
    def get_by_uuid(cls, uuid):
        obj = db.session.query(cls.model).filter_by(uuid=uuid).first()
        return obj

    @staticmethod
    def save_to_db(obj):
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete_from_db(obj):
        db.session.delete(obj)
        db.session.commit()
