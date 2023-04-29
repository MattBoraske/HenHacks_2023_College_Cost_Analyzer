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
wait = WebDriverWait(driver, 5)
search_bar = wait.until(EC.presence_of_element_located((By.ID, "searchbar-nav")))

# Click on the search bar to activate it
search_bar.click()

search_bar.send_keys("West Chester University")

time.sleep(1)


results = driver.find_element_by_css_selector("#searchbar-nav-results-container a")
time.sleep(2)
results.click()

current_url = driver.current_url
new_url = current_url + 'price/'
print(new_url)
time.sleep(1)

driver.get(new_url)

instate = driver.find_element_by_xpath('//div[@class="h2 mb-4"]')
instate = instate.text

tuition = driver.find_element_by_xpath('//td[@class="text-right font-weight-bold"]')
tuition = tuition.text

element = driver.find_element_by_xpath("//tr[2]/td[2]")
bookcost = element.text

element = driver.find_element_by_xpath("//tr[3]/td[2]")
other_fees = element.text

element = driver.find_element_by_xpath("//tr[4]/td[2]")
room_board = element.text

element = driver.find_element_by_xpath("//tr[5]/td[2]")
other_expenses = element.text


print(instate, tuition, bookcost, other_fees, room_board, other_expenses)

time.sleep(2)



# locate each row in the table and extract the cost information
