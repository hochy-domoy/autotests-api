from api_client_get_user import public_users_client
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_users_client, CreateFileRequest
from clients.private_http_builder import AuthenticationUserDict
from clients.users.puplic_user_clients import get_public_users_client, CreateRequestDict
from tools.fakers import get_random_email

public_user_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserDict(
    email=create_user_request["email"],
    password=create_user_request["password"],
)
files_client = get_files_users_client(authentication_user)
course_client = get_courses_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequest(
    filename='image.png',
    directory='courses',
    upload_file='./testdata/files/image.png',
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title='Python',
    maxScore=100,
    minScore=10,
    description='Python API course',
    estimatedTime="2 weeks",
    previewFileId=create_file_response["file"]["id"],
    createdByUserId=create_user_response["user"]["id"]
)
create_course_response = course_client.create_course(create_course_request)
print('Create course data:', create_course_response)