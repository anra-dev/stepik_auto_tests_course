import math
import pyperclip
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Основное задание
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    book = browser.find_element_by_id('book')
    book.click()

    # Решение задачи для робота
    tag_x = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "input_value")))
    value_x = tag_x.text

    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(calc(value_x))

    submit = browser.find_element_by_css_selector('button.btn[type="submit"]')
    submit.click()
    
    # Копируем ответ в буфер обмена
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    time.sleep(1)
    alert.accept()

finally:
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
