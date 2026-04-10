from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class ExerciseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class GetExercisesResponseSchema(BaseModel):
    exercises: list[ExerciseSchema]


class ExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema


class GetQueryRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    course_id: str


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания задания.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление данных задания.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    title: str | None
    max_score: int | None
    min_score: int | None
    order_index: int | None
    description: str | None
    estimated_time: str | None