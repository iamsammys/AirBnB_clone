#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """Details of User stored in this class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
