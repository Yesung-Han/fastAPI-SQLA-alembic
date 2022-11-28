from sqlalchemy import Column, Integer, String

from db.base_class import Base

class Teacher(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)