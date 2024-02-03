"""
Module containing Pydantic schemas for representing game categories and options.

These schemas are used for defining the structure of data objects related to game 
categories and options. 

They are implemented using Pydantic BaseModel, providing data validation 
and serialization capabilities.
"""

from pydantic import BaseModel


class GameCategorySchema(BaseModel):
    """
    Schema defining a game category
    """

    title: str


class OptionSchema(BaseModel):
    """
    Schema defining an Option
    """

    title: str
