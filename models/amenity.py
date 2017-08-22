#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, String, Table
from sqlalchemy.orm import relationship, backref
from os import getenv


class Amenity(BaseModel):
    """Amenity class handles all application amenities"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("PlaceAmenity", backref="amenities",
                                       cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
