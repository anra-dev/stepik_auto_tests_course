import math
import pyperclip
import time

from selenium import webdriver


link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    tag_x = browser.find_element_by_id('input_value')
    value_x = tag_x.text

    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(calc(value_x))

    submit = browser.find_element_by_css_selector('button.btn[type="submit"]')
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    time.sleep(2)
    alert.accept()

finally:
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
