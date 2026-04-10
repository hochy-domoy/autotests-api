from httpx import Client
from pydantic import BaseModel
# Импортируем модель LoginRequestSchema
from clients.authentication.authentication_client import get_authentication_client, LoginRequestSchema

# Добавили суффикс Schema вместо Dict
class AuthenticationUserSchema(BaseModel):  # Структура данных пользователя для авторизации
    email: str                              # Наследуем от BaseModel вместо TypedDict
    password: str

# Создаем private builder
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()

    # Используем модель LoginRequestSchema
    # Значения теперь извлекаем не по ключу, а через атрибуты

    # Инициализируем запрос на аутентификацию
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Добавляем заголовок авторизации
        # Значения теперь извлекаем не по ключу, а через атрибуты
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
    )