from sqlalchemy import Column, Integer, String

from app.db.base_class import Base

class Teacher(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(191), nullable=False, unique=True, index=True)