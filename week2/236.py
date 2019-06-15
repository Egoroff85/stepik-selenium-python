from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()

time.sleep(1)

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_id('input_value').text
y = calc(int(x))

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()