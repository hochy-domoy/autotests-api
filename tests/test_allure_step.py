import allure

@allure.step("Building api client")
def build_api_client():
    with allure.step("Get user authentication tokens"):
        ...

    with allure.step("Create new API client"):
        ...

@allure.step("Creating course with title {title}")
def create_course(title: str):
    ...

@allure.step("Deleting course")
def delete_course():
    ...

def test_feature():
    # with allure.step("Building API client"):
    #     ...
    #
    # with allure.step("Create course"):
    #     ...
    #
    # with allure.step("Deleting course"):
    #     assert False

    build_api_client()
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwrights")
    delete_course()
