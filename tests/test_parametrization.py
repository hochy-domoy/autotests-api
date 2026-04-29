import pytest
from _pytest.fixtures import SubRequest

# ТАК ДЕЛАТЬ НЕ НУЖНО:

# def test_number_1():
#     assert 1 > 0
#
# def test_number_2():
#     assert 2 > 0
#
# def test_number_3():
#     assert 3 > 0
#
# def test_number_minus_1():
#     for number in [-1, 1, 2, 3]:
#         assert number > 0

@pytest.mark.parametrize("number", [-1, 1, 2, 3])   # Параметризируем тест
# Название "number" в декораторе "parametrize" и в аргументах автотеста должны совпадать
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize("number, expected", [(1,1), (2,4), (3,9)])
# В данном случае в качестве данных используется список с кортежами
def test_several_numbers(number: int, expected: int):
    # Возводим число number в квадрат и проверяем, что оно равно ожидаемому
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"]) # Параметризируем по операционной системе
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com",
])  # Параметризируем по хосту
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0   # Проверка указана для примера

@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest) -> str:
    return request.param

def test_host(host: str):
    print(f"Running test on host: {host}")


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

users = {
    "+70000000011": "User with money on bank account",
    "70000000022": "User without money on bank account",
    "70000000033":  "User with operations on bank account"
}

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    pass