from clients.api_client import APIClient
from httpx import Response
# Добавили импорт моделей
from clients.authentication.authentication_schema import (LoginRequestSchema, RefreshRequestSchema,
                                                          LoginResponseSchema)
from clients.public_http_builder import get_public_http_client

# Старые модели с использованием TypedDict были удалены
class AauthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    def login_api(self, request : LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request.model_dump(by_alias=True))

    def refresh_api(self, request : RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))

    # Добавили метод login
    def login(self, request : LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request) # Отправляем запрос на аутентификацию
        #return LoginResponseSchema(**response.json()) # Извлекаем JSON из ответа, может выдать ошибку
        return LoginResponseSchema.model_validate_json(response.text) #response.text не вернет ошибку

# Добавляем builder для AuthenticationClient
def get_authentication_client() -> AauthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AauthenticationClient(client=get_public_http_client())
    #return AauthenticationClient(client=Client(timeout=100, base_url="https://localhost:8000")) аналогично этому