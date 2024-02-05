"""
Module defining Pydantic models for representing game data.

This module contains Pydantic BaseModel classes to represent various 
schemas related to games.
"""

from datetime import date, datetime
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

    id: int


class ResponseSubmissionBaseSchema(BaseModel):
    """Defines the base schema of a response submission"""

    game_id: int
    answer_id: int


class ResponseSubmissionInSchema(ResponseSubmissionBaseSchema):
    """Defines the input schema of a response submission"""

    pass


class ResponseSubmissionOutSchema(ResponseSubmissionBaseSchema):
    """Defines the output schema of a response submission"""

    is_correct: bool
    date_time: datetime
