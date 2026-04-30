import pytest
from pydantic import BaseModel
from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture

class CourseFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)

@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> CourseFixture:
    request = CreateFileRequestSchema()
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)