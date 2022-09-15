from selenium import webdriver
chrome_driver_path = r"/home/amrutraj/PycharmProjects/Python/Day48/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://python.org')
s = driver.find_element("xpath", '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
fin = dict()
inf = s.text.split('\n')
num = 0
for i in range(0, len(inf), 2):
    fin[num] = {'time':inf[i], 'event':inf[i+1]}
    num += 1
print(fin)
driver.quit()
