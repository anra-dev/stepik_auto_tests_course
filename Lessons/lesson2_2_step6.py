import math
import time

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    tag_x = browser.find_element_by_id('input_value')
    value_x = tag_x.text

    input_answer = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    input_answer.send_keys(calc(value_x))

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    robots_rule = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
    robots_rule.click()

    submit = browser.find_element_by_css_selector('button.btn[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
