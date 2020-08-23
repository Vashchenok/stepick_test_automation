from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("input.first")
    first_name.send_keys("SOme text")

    second_name = browser.find_element_by_css_selector("input.second")
    second_name.send_keys("dawdaw")

    email = browser.find_element_by_css_selector("input.third")
    email.send_keys("dwadaw")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    time.sleep(1)


    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()