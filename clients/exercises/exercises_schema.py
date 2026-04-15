from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from tools.fakers import Fake, fake


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

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(default_factory=fake.uuid4)
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    order_index: int = Field(default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление данных задания.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    order_index: int | None = Field(default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)