import os
import time

from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Ivan")

    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Petrov")

    email = browser.find_element_by_name("email")
    email.send_keys("mail@domain.net")

    file_field = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file_field.send_keys(file_path)

    submit = browser.find_element_by_css_selector('button.btn[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
