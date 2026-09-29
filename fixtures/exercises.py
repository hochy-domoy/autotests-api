import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema
from fixtures.courses import function_course, CourseFixture
from fixtures.users import UserFixture

class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: ExerciseResponseSchema

@pytest.fixture
def exercise_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(
    exercise_client: ExercisesClient,
    function_course: CourseFixture
    ) -> ExerciseFixture:
    response = CreateExerciseRequestSchema(
        course_id=function_course.response.course.id
    )
    request = exercise_client.create_exercise(response)
    return ExerciseFixture(request=response, response=request)