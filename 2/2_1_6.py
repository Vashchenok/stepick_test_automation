from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_erl = browser.find_element_by_id("treasure")
    x = x_erl.get_attribute("valuex")
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    time.sleep(1)
    browser.find_element_by_css_selector("button").click()


finally:
    time.sleep(5)
    browser.quit()
