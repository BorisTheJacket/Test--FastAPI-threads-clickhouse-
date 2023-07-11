from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, Text
from db import engine


class EtgbDeclaration(declarative_base(bind=engine)):
    __tablename__ = 'etgb_declaration'
    id=Column('id', Integer, primary_key=True)
    posting_number=Column('posting_number', Text)
    number=Column('number', Text)
    date=Column('date', Text)
    url=Column('url', Text)

    def __repr__(self):
        return f'{self.id}'