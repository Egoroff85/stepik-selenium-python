from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

x = browser.find_element_by_id('num1').text
y = browser.find_element_by_id('num2').text
result = int(x) + int(y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(result))

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()
