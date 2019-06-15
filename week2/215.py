from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x_element = browser.find_element_by_id('input_value')
x = int(x_element.text)
y = calc(x)

answer = x_element = browser.find_element_by_id('answer')
answer.send_keys(y)

robot_checkbox = browser.find_element_by_id('robotCheckbox')
robot_checkbox.click()

robot_rules = browser.find_element_by_id('robotsRule')
robot_rules.click()

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()