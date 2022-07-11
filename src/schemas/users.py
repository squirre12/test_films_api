from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.database.models import User


class UsersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('id', 'is_admin')
        load_instance = True
        load_only = ('password',)