from selenium import webdriver  # 获得浏览器驱动
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
url = 'http://10.200.0.2'
driver.get(url)
driver.implicitly_wait(5)
driver.find_elements(By.CLASS_NAME, 'edit_lobo_cell')[2].send_keys('')
driver.find_elements(By.CLASS_NAME, 'edit_lobo_cell')[3].send_keys('')


el1 = driver.find_element(By.CSS_SELECTOR, 'div [class="edit_lobo_cell edit_radio"] > span [value="@telecom"]')  # 用css层级搜索找到“中国电信”左边那个小圆圈
driver.execute_script("arguments[0].click();", el1)  # 普通点击方法无效，用js点击
el2 = driver.find_elements(By.CLASS_NAME, 'edit_lobo_cell')[1]
driver.execute_script("arguments[0].click();", el2)  # 普通点击方法无效，用js点击
sleep(1)
driver.close()
