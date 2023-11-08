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

# Find the search input field by name attribute and enter the search query
search_box = driver.find_element(By.NAME, "username")
search_box.send_keys("PICT")
driver.implicitly_wait(10)  # 5 seconds
search_box1 = driver.find_element(By.NAME, "password")
search_box1.send_keys("GANAPATI")
#search_box.submit()
search_box1.submit()
# Wait for a while to see the search results (you might need to adjust the time)
driver.implicitly_wait(10)  # 10 seconds

# Print the title of the current page (optional)
#print("Page Title: " + driver.title)
driver.close()
print("sample test case successfully completed")