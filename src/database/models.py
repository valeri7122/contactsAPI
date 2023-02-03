from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(50), nullable=False, unique=True)
    birthday = Column(String(50), nullable=False)
    optionaly = Column(String(100), nullable=True)
    done = Column(Boolean, default=False)
    created_at = Column('created_at', DateTime, default=func.now(), nullable=False)
