from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id("input_value").text
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)

browser.find_element_by_id("robotCheckbox").click()

browser.execute_script("window.scrollBy(0, 100);")

browser.find_element_by_id("robotsRule").click()
time.sleep(1)
browser.find_element_by_css_selector("button").click()



time.sleep(10)
browser.quit()
