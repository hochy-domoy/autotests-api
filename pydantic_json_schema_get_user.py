from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.puplic_user_clients import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, UserSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

# Создаем клиента
public_user_client = get_public_users_client()

# Отправляем POST запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email= get_random_email(),
    password= "string",
    last_name= "string",
    first_name= "string",
    middle_name= "string"
)
create_user_response = public_user_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()

# Инициализируем клиенты
authentication_client_response = AuthenticationUserSchema(
    email= create_user_request.email,
    password= create_user_request.password
)
private_user_client = get_private_users_client(authentication_client_response)

# Отправляем GET запрос на получение данных пользователя
get_user_response_client = private_user_client.get_user_api(create_user_response_json['user']['id']).json()

#Генерируем JSON схему для ответа GET запроса
user_request = UserSchema(
    id= "string",
    email= get_random_email(),
    last_name= "string",
    first_name= "string",
    middle_name= "string"
)

get_user_response = GetUserResponseSchema(
    user= user_request
)

get_user_response_schema = get_user_response.model_json_schema()

#Валидируем ответ GET запроса
validate_json_schema(instance=get_user_response_client, schema=get_user_response_schema)

