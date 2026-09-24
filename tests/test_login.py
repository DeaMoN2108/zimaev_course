import pytest, allure

@allure.feature("Login page")
@allure.title("Авторизвация с недействительными учётными данными")
@allure.severity(allure.severity_level.NORMAL)
def test_login_fail(login_page):
    with allure.step("Открыть страницу авторизации"):
        login_page.navigate_to_login_page()
    with allure.step("Ввести в форму авторизации недействительные учётные данные"):
        login_page.login("invalid_username", "invalid_password")
    with allure.step("Проверка, что URL не изменился"):
        assert login_page.get_current_url() == login_page.URL
    with allure.step("Проверка корректно сообщения об ошибке"):
        assert login_page.get_error_msg() == "Invalid credentials. Please try again."


@pytest.mark.parametrize("username,password", [("admin", "admin"), ("user", "user")])
@allure.feature("Login page")
@allure.title("Авторизация с корректными учётными данными")
@allure.severity(allure.severity_level.NORMAL)
def test_login_success(login_page, dashboard_page, username, password):
    with allure.step("Открыть страницу авторизации"):
        login_page.navigate_to_login_page()
    with allure.step("Ввести в форму авторизации корректные учётные данные"):
        login_page.login(username, password)
    with allure.step("Проверка, что отображается приветственное сообщение с верным username"):
        dashboard_page.assert_welcome_message(f"Welcome {username}")