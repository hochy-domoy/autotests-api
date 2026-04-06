"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
import uuid

# Добавили модель FileSchema
class FileSchema(BaseModel):
    id: str
    url: HttpUrl    # Используем HttpUrl вместо str
    filename: str
    directory: str

# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr     # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field  #динамически сформированное поле (при сиреллиз. и диссерилиз. будет это поле)
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseShema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True) #если знаем, что все поля в каком-то едином формате
    id: str = Field(default_factory=lambda: str(uuid.uuid4())) #lambda - это анонимная функция
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright"
    # Вложенный объект для файла-превью
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    # Вложенный объект для пользователя, создавшего курс
    created_by_user: UserSchema = Field(alias="createdByUser")

# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseShema(
    id="course_id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    # Добавили инициализацию вложенной модели FileSchema
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses"
    ),
    estimatedTime="1 week",
    # Добавили инициализацию вложенной модели UserSchema
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alice"
    )
)

print(f"Course default model: {course_default_model}",
      f"Type course default model: {type(course_default_model)}", sep="\n", end="\n\n")

# Инициализируем модель CourseSchema через распаковку словаря
course_dict ={      #словарь
    "id": "course_id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    # Добавили ключ previewFile
    "previewFile": {
        "id":"file-id",
        "url":"http://localhost:8000",
        "filename":"file.png",
        "directory":"courses"
    },
    "estimatedTime": "1 week",
    # Добавили ключ createdByUser
    "createdByUser": {
        "id":"user-id",
        "email":"user@gmail.com",
        "lastName":"Bond",
        "firstName":"Zara",
        "middleName":"Alice"
    }
  }

course_dict_model = CourseShema(**course_dict)
print(f"Course dict model: {course_dict_model}",
      f"Type course dict model: {type(course_dict)}", sep="\n", end="\n\n")

#json строка
# Инициализируем модель CourseSchema через JSON
course_json = """    
{      
    "id": "course_id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id":"file-id",
        "url":"http://localhost:8000",
        "filename":"file.png",
        "directory":"courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id":"user-id",
        "email":"user@gmail.com",
        "lastName":"Bond",
        "firstName":"Zara",
        "middleName":"Alice"  
    }
  }

"""
course_json_model = CourseShema.model_validate_json(course_json)
print(f"Course json model: {course_json_model}",
      f"Type course json model: {type(course_json)}", sep="\n", end="\n\n")
#Диссерилизация
print(f"CourseShema -> dict: {course_json_model.model_dump()}",
      f"Type course_json_model.model_dump(): {type(course_json_model.model_dump())}", sep="\n", end="\n\n")

print(f"CourseShema -> json-строка: {course_json_model.model_dump_json()}",
      f"Type course_json_model.model_dump_json(): {type(course_json_model.model_dump_json())}", sep="\n", end="\n\n")
#snake_case -> camelCase
print(f"CourseShema -> dict: {course_json_model.model_dump(by_alias=True)}",
      f"Type course_json_model.model_dump(by_alias=True): {type(course_json_model.model_dump())}", sep="\n", end="\n\n")

print(f"CourseShema -> json-строка: {course_json_model.model_dump_json(by_alias=True)}",
      f"Type course_json_model.model_dump_json(by_alias=True): {type(course_json_model.model_dump_json())}", sep="\n", end="\n\n")

user = UserSchema(
    id="user-id",
    email="user@gmail.com",
    lastName="Bond",
    firstName="Zara",
    middleName="Alice"
)
print(user.get_username(), user.username)

# Инициализируем FileSchema c некорректным url
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses"
    )
except ValidationError as error:
    print(error)
    print(error.errors())