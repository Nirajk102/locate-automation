from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pytest


driver=webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.facebook.com")
print(driver.title)
print(driver.current_url)
driver.quit()