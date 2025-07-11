from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/text-box")

# driver.find_element(By.ID, "userName").send_keys("Rianto")
# driver.find_element(By.ID, "submit").click()

print("Test berhasil dijalankan!")
driver.quit()