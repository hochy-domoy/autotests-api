from typing import Any, Sized

from clients.users.users_schema import UserSchema, GetUserResponseSchema, CreateUserResponseSchema



def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, (
        'Incorrect response status code.'
        f'Expected status code: {expected}.'
        f'Actual status code: {actual}'
    )

def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expected, (
        f'Incorrect value: "{name}".'
        f'Expected value: "{expected}".'
        f'Actual value: "{actual}"'
    )


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )

def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет корректность данных пользователя.

    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.email, expected.email, 'email')
    assert_equal(actual.last_name, expected.last_name, 'last_name')
    assert_equal(actual.first_name, expected.first_name, 'first_name')
    assert_equal(actual.middle_name, expected.middle_name, 'middle_name')

def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет, что данные пользователя при создании и при запросе совпадают.

    :param get_user_response: Ответ API при запросе пользователя.
    :param create_user_response: Ответ API при создании пользователя.
    """
    assert_user(actual=get_user_response.user, expected=create_user_response.user)

def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    assert len(actual) == len(expected), (
        f'Incorrect object length: "{name}". '
        f'Expected length: {len(actual)}.' 
        f'Actual length: {len(actual)}'
    )