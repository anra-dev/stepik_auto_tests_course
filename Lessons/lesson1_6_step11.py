import time

from selenium import webdriver


try: 
    link = "http://suninjuly.github.io/registration1.html"
    # Для проверки второй части задания закомментируй строку выше 
    # и разкомментируй строку ниже 
    # link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element_first = browser.find_element_by_css_selector('input.form-control.first[required]')
    element_first.send_keys("Мой first-ответ")
    element_second = browser.find_element_by_css_selector('input.form-control.second[required]')
    element_second.send_keys("Мой second-ответ")
    element_third = browser.find_element_by_css_selector('input.form-control.third[required]')
    element_third.send_keys("Мой third-ответ")
    time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
