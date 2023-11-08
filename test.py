'''from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome()
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.google.com/")
#identify the Google search text box and enter the value
#driver.find_element_by_name("q").send_keys("javatpoint")
driver.find_element("javatpoint", "q")
time.sleep(3)
#click on the Google search button
driver.find_element("btnK").send_keys(Keys.ENTER)
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")'''

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
#navigate to the url

driver.get("https://mail.google.com/")

# Find the email input field and enter your email address
email_field = driver.find_element(By.ID, 'identifierId')
email_field.send_keys("4b72021@gmail.com")

# Click the 'Next' button
email_field.send_keys(Keys.RETURN)

# Wait for a while to load the password input field (you might need to adjust the time)
driver.implicitly_wait(5)  # 5 seconds

# Find the password input field and enter your password
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys("4B72021@FE")

# Click the 'Next' button to log in
password_field.send_keys(Keys.RETURN)

# Wait for the login process to complete (you might need to adjust the time)
driver.implicitly_wait(10)  # 10 seconds

# Verify if the login was successful (you can add more verifications as needed)
if "inbox" in driver.current_url.lower():
    print("Login successful!")
else:
    print("Login failed.")
#close the browser
driver.close()
print("Gmail login has been successfully completed")