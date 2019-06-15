from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")

x = browser.find_element_by_id('input_value').text
result = calc(int(x))

answer = browser.find_element_by_id('answer')
answer.send_keys(result)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

robot_checkbox = browser.find_element_by_id('robotCheckbox')
robot_checkbox.click()

robot_rules = browser.find_element_by_id('robotsRule')
robot_rules.click()

button.click()
