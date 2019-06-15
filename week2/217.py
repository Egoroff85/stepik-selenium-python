from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

x = browser.find_element_by_id('treasure').get_attribute('valuex')
y = calc(int(x))

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

robot_checkbox = browser.find_element_by_id('robotCheckbox')
robot_checkbox.click()

robot_rules = browser.find_element_by_id('robotsRule')
robot_rules.click()

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()
