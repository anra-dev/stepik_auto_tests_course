import time
import math
import pytest
import warnings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
    ]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def answer():
    return math.log(int(time.time()))


@pytest.mark.parametrize('link', links)
def test_stepik_task_solution(browser, answer, link):
    browser.get(link)
    
    text_area = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-text-area")))
    text_area.send_keys(answer)

    submit = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".submit-submission")))
    submit.click()

    feedback = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    
    assert feedback.text == "Correct!", f"Ответ для {link} неверный"
