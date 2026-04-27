import pytest
from clients.authentication.authentication_client import get_authentication_client, AauthenticationClient

@pytest.fixture # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def authentication_client() -> AauthenticationClient:   # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API-клиент для работы с аутентификацией
    return get_authentication_client()

