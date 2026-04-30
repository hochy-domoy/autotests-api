from http import HTTPStatus
from clients.authentication.authentication_client import get_authentication_client, AauthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.puplic_user_clients import get_public_users_client, PublicUserClient
from clients.users.users_schema import CreateUserRequestSchema
from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
import pytest

@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:
    def test_login(self,
            function_user: UserFixture,  # Используем фикстуру для создания пользователя
            authentication_client: AauthenticationClient
        ):
        # Запрос на логин (login_request -> request)
        request = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password,
        )
        # Выполняем логин (login_response -> response)
        response = authentication_client.login_api(request)
        # Валидация ответа (login_response_data -> response_data)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        # Используем функцию для проверки статус-кода
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Используем функцию для проверки ответа аутентификации юзера
        assert_login_response(response_data)
        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())