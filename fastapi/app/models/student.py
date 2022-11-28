from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.base_class import Base

# if TYPE_CHECKING:
#     from .teacher import Teacher  # noqa: F401

class Student(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    nickname = Column(String, unique=True, nullable=False, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    time_updated = Column(DateTime(timezone=True), onupdate=func.utcnow(), nullable=False)