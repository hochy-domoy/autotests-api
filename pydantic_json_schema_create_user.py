from clients.authentication.authentication_schema import TokenSchema
from clients.users.puplic_user_clients import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email
import jsonschema

#print(TokenSchema.model_json_schema())

schema = {
    'description': 'Описание структуры аутентификационных токенов.',
    'properties': {
        'tokenType': {'title': 'Tokentype', 'type': 'string'},
        'accessToken': {'title': 'Accesstoken', 'type': 'string'},
        'refreshToken': {'title': 'Refreshtoken', 'type': 'string'}
    },
    'required': ['tokenType', 'accessToken', 'refreshToken'],
    'title': 'TokenSchema',
    'type': 'object'
}
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
public_users_client = get_public_users_client()
# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()
#del create_user_response_json['user']['email']
#print(create_user_response_schema)
#print(create_user_response.json())
#create_user_response_json['user']['email'] = "hello"
#jsonschema.validate(instance=create_user_response_json, schema=create_user_response_schema)
validate_json_schema(instance=create_user_response_json, schema=create_user_response_schema)