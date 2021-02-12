from selenium import webdriver

driver = webdriver.Chrome()

url = driver.command_executor._url
session_id = driver.session_id

# webdriver.driver.attachToSession(executor, session_id);

# chrome_path = C:\Program Files (x86)\Google\Chrome\Application

