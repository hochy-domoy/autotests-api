from clients.users.private_users_client import PrivateUsersClient
from clients.users.puplic_user_clients import PublicUserClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
# Импортируем функцию проверки статус-кода
from tools.assertions.base import assert_status_code, assert_get_user_response
# Импортируем функцию для валидации JSON Schema
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import assert_create_user_response
import pytest
from tools.fakers import fake

@pytest.mark.users
@pytest.mark.regression
class TestUsers():
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self, public_users_client: PublicUserClient, domain: str):
        # Формируем тело запроса на создание пользователя
        request = CreateUserRequestSchema(
            email=fake.email(domain)
        )
        print(request)
        # Отправляем запрос на создание пользователя
        response = public_users_client.create_user_api(request)
        # Валидация ответа (login_response_data -> response_data)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # Используем функцию для проверки статус-кода
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Используем функцию для проверки ответа создания юзера
        assert_create_user_response(request, response_data)
        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_user_me(self, private_users_client: PrivateUsersClient, function_user):
        # Отправляем запрос на получение пользователя
        response = private_users_client.get_users_me_api()
        # Валидация ответа (login_response_data -> response_data)
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        # Используем функцию для проверки статус-кода
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Используем функцию для проверки ответа получения юзера
        assert_get_user_response(response_data, function_user.response)
        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())