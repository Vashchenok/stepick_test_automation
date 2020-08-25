from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects1.html"



browser = webdriver.Chrome()
browser.get(link)

sum = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum))
 

browser.find_element_by_css_selector("button").click()


time.sleep(11)
browser.quit()
    