from pydantic import BaseModel, Field
from tools.fakers import fake

# Добавили суффикс Schema вместо Dict
class TokenSchema(BaseModel):   # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias='tokenType')  # Использовали aliase
    access_token: str = Field(alias='accessToken')  # Использовали aliase
    refresh_token: str = Field(alias='refreshToken')    # Использовали aliase

# Добавили суффикс Schema вместо Dict
class LoginRequestSchema(BaseModel):    # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email)      #Модель в данном виде можно использовать только для негативного теста, т.к. для логина нужны не случайные данные
    password: str = Field(default_factory=fake.password)    #Когда вызывается эта модель, нужно передавать в нее валидные данные

# Добавили суффикс Schema вместо Dict
class LoginResponseSchema(BaseModel):   # Наследуем от BaseModel вместо TypedDict
    token: TokenSchema

# Добавили суффикс Schema вместо Dict
class RefreshRequestSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias='refreshToken', default_factory=fake.sentence)    # Использовали aliase