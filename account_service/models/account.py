from books_shared.utils import logger

from books_shared.utils.db import db


class AccountModel(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def fynd_by_id(cls, id):
        logger.info(f"Find by id {id}")
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_email(cls, email):
        logger.info(f"Find by email {email}")
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_all(cls):
        logger.info("Find all accounts")
        return cls.query.all()

    def save_to_db(self):
        logger.info(f"Save Account {self} to db")
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Account: name {self.name} email{self.email}"

    def __str__(self):
        return f"Account: name {self.name} email{self.email}"
