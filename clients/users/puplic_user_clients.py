from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.public_http_builder import get_public_http_client

class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id:str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    user: User

class PublicUserClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request : CreateRequestDict) -> Response:
        """
        Метод создает нового пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    # Добавили новый метод
    def create_user(self, request: CreateRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUserClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUserClient(client=get_public_http_client())