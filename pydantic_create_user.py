import uuid
from pydantic import BaseModel, Field, ConfigDict, EmailStr, constr
from pydantic.alias_generators import to_camel

class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: constr(min_length=1, max_length=50)
    first_name: constr(min_length=1, max_length=50)
    middle_name: constr(min_length=1, max_length=50)

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    email: EmailStr
    password: constr(min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50)
    first_name: constr(min_length=1, max_length=50)
    middle_name: constr(min_length=1, max_length=50)

class CreateUserResponseDict(BaseModel):
    """
    Описание структуры ответа на создание пользователя.
    """
    user: UserSchema