
from pydantic import BaseModel


class GameCategorySchema(BaseModel):
    """
    Pydantic schema for game category
    """
    title: str
