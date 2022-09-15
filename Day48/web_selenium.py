from selenium import webdriver
chrome_driver_path = r"/home/amrutraj/PycharmProjects/Python/Day48/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://kite.zerodha.com')
