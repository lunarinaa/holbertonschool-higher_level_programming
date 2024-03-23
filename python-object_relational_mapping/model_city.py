#!/usr/bin/python3
"""class that inherits from base"""


from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """class definition"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
