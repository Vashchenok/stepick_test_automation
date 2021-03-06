from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector("button").click()

second_window = browser.window_handles[1]
browser.switch_to.window(second_window)

x_erl = browser.find_element_by_id("input_value")
x = x_erl.text
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_css_selector("button").click()