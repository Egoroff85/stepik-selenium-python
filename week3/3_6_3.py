import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


links = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', links)
def test_all_urls_in_the_list(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)
    answer_input = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea.string-quiz__textarea'))
    )
    answer_input.clear()
    answer = str(math.log(int(time.time())))
    answer_input.send_keys(answer)
    submit_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))
    )
    submit_button.click()
    WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".attempt-message_correct"))
    )
    feedback = browser.find_element_by_css_selector('pre.smart-hints__hint')
    assert feedback.text == 'Correct!', str(feedback.text)