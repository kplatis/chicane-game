"""
Module defining Pydantic models for representing game data.

This module contains Pydantic BaseModel classes to represent various 
schemas related to games.
"""

from datetime import date
from pydantic import BaseModel


class GameBaseSchema(BaseModel):
    """
    Schema defining a game
    """

    question: str
    date: date
    category_id: int


class GameInSchema(GameBaseSchema):
    """
    Schema defining the input of a game
    """

    correct_answer_id: int


class GameOutSchema(GameBaseSchema):
    """
    Schema defining the output of a game
    """

    pass
