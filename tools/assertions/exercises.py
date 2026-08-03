import allure
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema, ExerciseSchema, \
    GetExercisesResponseSchema, GetExerciseResponseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_response
from tools.logger import get_logger

logger = get_logger("EXERCISES_ASSERTIONS")

@allure.step("Check create exercise response")
def assert_create_exercise_response(
        response:CreateExerciseRequestSchema,
        request:ExerciseResponseSchema
    ):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create exercise response")

    assert_equal(response.title, request.exercise.title, "title")
    assert_equal(response.course_id, request.exercise.course_id, "course_id")
    assert_equal(response.min_score, request.exercise.min_score, "min_score")
    assert_equal(response.max_score, request.exercise.max_score, "max_score")
    assert_equal(response.order_index, request.exercise.order_index, "order_index")
    assert_equal(response.description, request.exercise.description, "description")
    assert_equal(response.estimated_time, request.exercise.estimated_time, "estimated_time")

@allure.step("Check exercise")
def assert_exercise(
        response:ExerciseSchema,
        request:ExerciseSchema
    ):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check exercise")

    assert_equal(response.id, request.id, "id")
    assert_equal(response.course_id, request.course_id, "course_id")
    assert_equal(response.min_score, request.min_score, "min_score")
    assert_equal(response.max_score, request.max_score, "max_score")
    assert_equal(response.order_index, request.order_index, "order_index")
    assert_equal(response.description, request.description, "description")
    assert_equal(response.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Check get exercise response")
def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: ExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение задания соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных задания.
    :param create_exercise_response: Ответ API при создании задания.
    :raises AssertionError: Если данные файла не совпадают.
    """
    logger.info("Check get exercise response")

    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(
        response: UpdateExerciseResponseSchema,
        request: UpdateExerciseRequestSchema
        ):
    """
    Проверяет, что ответ на обновление задания соответствует данным из запроса.

    :param request: Исходный запрос на обновление задания.
    :param response: Ответ API с обновленными данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check update exercise response")

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    logger.info("Check exercise not found response")

    expected = InternalErrorResponseSchema(detail="Exercise not found")
    assert_internal_response(actual, expected)

@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_responses: GetExercisesResponseSchema,
        create_responses: list[ExerciseResponseSchema]
    ):
    """
    Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

    :param get_responses: Ответ API при запросе списка заданий.
    :param create_responses: Список API ответов при создании заданий.
    :raises AssertionError: Если данные заданий не совпадают.
    """
    logger.info("Check get exercises response")

    assert_length(get_responses.exercises, create_responses, "exercises")
    for index, create_exercise in enumerate(create_responses):
        assert_exercise(get_responses.exercises[index], create_exercise.exercise)