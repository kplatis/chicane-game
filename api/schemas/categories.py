from pydantic import BaseModel


class GameCategoryBaseSchema(BaseModel):

    title: str


class GameCategoryInSchema(GameCategoryBaseSchema):
    """
    Schema defining a game category
    """

    pass


class GameCategoryOutSchema(GameCategoryBaseSchema):
    """
    Schema defining a game category
    """

    id: int


class OptionBaseSchema(BaseModel):
    """
    Schema defining the base of an option
    """

    title: str


class OptionInSchema(OptionBaseSchema):
    """
    Schema defining the input of an Option
    """

    pass


class OptionOutSchema(OptionBaseSchema):
    """
    Schema defining the output of an Option
    """

    id: int
    category_id: int

    class Config:
        orm_mode = True
