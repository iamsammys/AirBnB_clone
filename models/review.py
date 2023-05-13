#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Storing up review of a place for a user"""
    place_id = ""
    user_id = ""
    text = ""
