from selenium import webdriver
import os


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")


first_name = browser.find_element_by_css_selector('input[name="firstname"]')
first_name.send_keys('Ivan')

last_name = browser.find_element_by_css_selector('input[name="lastname"]')
last_name.send_keys('Petrov')

last_name = browser.find_element_by_css_selector('input[name="lastname"]')
last_name.send_keys('Petrov')

email = browser.find_element_by_css_selector('input[name="email"]')
email.send_keys('IvanPetrov@gmail.com')


file_input = browser.find_element_by_id('file')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
file_input.send_keys(file_path)

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()
