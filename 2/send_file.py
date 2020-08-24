from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_name("firstname").send_keys("dwada")
browser.find_element_by_name("lastname").send_keys("dwada")
browser.find_element_by_name("email").send_keys("dwada")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
browser.find_element_by_id("file").send_keys(file_path)

browser.find_element_by_css_selector("button").click()