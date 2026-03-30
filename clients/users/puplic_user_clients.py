from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class CreateRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

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
        return self.post("/api/v1/authentication/login", json=request)