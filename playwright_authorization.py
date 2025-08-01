from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()  # Создаем новую страницу

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим поле "Email" и заполняем его
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    # Находим поле "Password" и заполняем его
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # Находим кнопку "Login" и кликаем на нее  -  по новому локатору
    login_button = page.get_by_test_id('registration-page-registration-button')
    login_button.click()

    # Проверяем, что появилось сообщение об ошибке
    dashboard_text = page.locator('//div[@class="MuiBox-root css-70qvj9"]/h6')
    expect(dashboard_text).to_be_visible()  # Проверяем видимость элемента
    expect(dashboard_text).to_have_text("Dashboard")  # Проверяем текст

    # Пауза на 5 секунд, чтобы увидеть результат ТОЛЬКО ДЛЯ ДЕМО
    page.wait_for_timeout(5000)