from playwright.sync_api import Page

class LoginPage(Page):
    URL = "https://zimaev.github.io/pom/"
    def __init__(self, page: Page):
        """Объявление переменных"""
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login")
        self.error_msg = page.locator("#errorAlert")

    def navigate_to_login_page(self):
        """Открывает страницу логина"""
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        """Выполняем вход в учётную запись с заданными данными"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_msg(self):
        """Возвращает текст сообщения об ошибке"""
        return self.error_msg.inner_text()

    def get_current_url(self):
        """Проверяем, что находимся на странице логин"""
        return self.page.url