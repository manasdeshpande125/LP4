from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
print("test case started")
#open Google Chrome browser
driver = webdriver.Chrome()
#maximize the window size
driver.maximize_window()
#delete the cookies
driver.delete_all_cookies()
driver.get("http://127.0.0.1:8000/")
search_box = driver.find_element(By.NAME, "username")
search_box.send_keys("PICT")
driver.implicitly_wait(10)  # 5 seconds
search_box1 = driver.find_element(By.NAME, "password")
search_box1.send_keys("GANAPATI")
#search_box.submit()
search_box1.submit()
driver.implicitly_wait(5)  # 5 seconds
submit_button = driver.find_element(By.NAME, "add")
submit_button.click()


# Find the search input field by name attribute and enter the search query
search_box = driver.find_element(By.NAME, "title")
search_box.send_keys("Selenium")
driver.implicitly_wait(5)  # 5 seconds
search_box1 = driver.find_element(By.NAME, "description")
search_box1.send_keys("MINIPROJECT")
print("success")
search_box2 = driver.find_element(By.NAME, "support")
search_box2.send_keys("100")
file_input = driver.find_element(By.NAME, "certificate")
file_input.send_keys(r"C:\Users\Admin\Downloads\Manas_Deshpande_Ace.pdf")
#search_box2.submit()
submit_button = driver.find_element(By.NAME, "submit")
submit_button.click()


driver.close()
print("sample test case successfully completed")