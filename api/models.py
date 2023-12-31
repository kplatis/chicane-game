from tortoise import fields, Model


class Game(Model):
    id = fields.IntField(pk=True)
    question = fields.CharField(max_length=300)
    date = fields.DateField()
    category = fields.ForeignKeyField("models.GameCategory", related_name="games")


class GameCategory(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    games = fields.ReverseRelation["Game"]


class Response(Model):
    id = fields.IntField(pk=True)
    category = fields.ForeignKeyField("models.GameCategory", related_name="responses")
    title = fields.CharField(max_length=300)
