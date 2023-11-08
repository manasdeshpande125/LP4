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
driver.get("https://www.google.com")

# Find the search input field by name attribute and enter the search query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Mango")

# Submit the search form
search_box.submit()

# Wait for a while to see the search results (you might need to adjust the time)
driver.implicitly_wait(10)  # 10 seconds

# Print the title of the current page (optional)
print("Page Title: " + driver.title)
driver.close()
print("sample test case successfully completed")