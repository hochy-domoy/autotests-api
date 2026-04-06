from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")
    is_private: bool = True # Значение по умолчанию

user_data = {
    'id':1,
    'name':'Alice',
    'email':'alice@example.com',
    'isActive':True
}

user = User(**user_data)

print(user.model_dump(), type(user.model_dump())) # Выводит словарь
print(user.model_dump_json(), type(user.model_dump_json())) # Выводит JSON-строку


