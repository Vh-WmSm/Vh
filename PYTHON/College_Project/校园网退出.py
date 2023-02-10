from selenium import webdriver  # 获得浏览器驱动
from selenium.webdriver.common.by import By
from pyautogui import press


driver = webdriver.Chrome()
url = 'http://10.200.0.2'
driver.get(url)
driver.implicitly_wait(5)
el = driver.find_element(By.CLASS_NAME, 'btn')
driver.execute_script("arguments[0].click();", el)
driver.implicitly_wait(3)
press('enter')
driver.close()
