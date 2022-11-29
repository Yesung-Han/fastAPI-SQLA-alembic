from typing import TYPE_CHECKING
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .teacher import Teacher  # noqa: F401

class Lecture(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(191), nullable=False, unique=True, index=True)
    description = Column(String(191))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable=False) # oneToMany
    teacher = relationship("Teacher", back_populates="lectures") # oneToMany