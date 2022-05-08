import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    tag_num1 = browser.find_element_by_id('num1')
    value_num1 = tag_num1.text

    tag_num2 = browser.find_element_by_id('num2')
    value_num2 = tag_num2.text

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(value_num1)+int(value_num2)))

    submit = browser.find_element_by_css_selector('button.btn[type="submit"]')
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
