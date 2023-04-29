import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Create a ChromeDriver instance using ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# Navigate to the website
driver.get('https://www.collegesimply.com/')

# Wait for the search bar to be located on the page
wait = WebDriverWait(driver, 10)
search_bar = wait.until(EC.presence_of_element_located((By.ID, "searchbar-nav")))

# Click on the search bar to activate it
search_bar.click()

# Type "the" into the search bar
search_bar.send_keys("West Chester University")


# Press Enter to submit the search
#search_bar.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(10)

# Extract the page title
title = driver.title
print(title)

