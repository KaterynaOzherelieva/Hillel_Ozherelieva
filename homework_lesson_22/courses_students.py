from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from homework_lesson_22.declarative_base import Base

class Club(Base):
    __tablename__ = 'club'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    students = relationship("Students", back_populates="club")


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    club_id = Column(Integer, ForeignKey('club.id'))

    club = relationship("Club", back_populates="students")



