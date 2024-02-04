"""
Module defining Pydantic models for representing game data.

This module contains Pydantic BaseModel classes to represent various 
schemas related to games.
"""

from datetime import date
from pydantic import BaseModel


class GameBaseSchema(BaseModel):
    """
    Defines the base schema for a game
    """

    question: str
    date: date
    category_id: int


class GameInSchema(GameBaseSchema):
    """
    Defines the input schema for a game
    """

    correct_answer_id: int


class GameOutSchema(GameBaseSchema):
    """
    Defines the output schema for a game
    """

    pass
