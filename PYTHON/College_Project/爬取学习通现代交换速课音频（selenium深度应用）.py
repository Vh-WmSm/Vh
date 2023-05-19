from selenium import webdriver  # 获得浏览器驱动
import requests
from selenium.webdriver.common.by import By
import os

# def open_(address, num, content):
#     with open(address + '\\' + num + '.txt', 'w', encoding='gb18030') as f:
#         f.write(content)

# address = 'c:\\users\\vh\\desktop'

address = input('下载到：')
unit = int(input('第几章：'))
lesson = int(input('这章的第几节课：'))
frames = int(input('这节课的有几个iframe：'))

os.chdir(address)
for i in range(frames):  # 在目标文件夹创建frames个文件夹并编号为1、2、3……
    try:
        os.mkdir(str(i + 1))
    except:
        pass

driver = webdriver.Edge()  # 直接这样写是打开浏览器窗口运行，如果要静默运行则以下代码

# driver_options = webdriver.EdgeOptions()
# driver_options.add_argument('--headless')
# driver = webdriver.Edge(options=driver_options)

url = 'http://passport2.chaoxing.com/login?fid=1055&refer=http://i.mooc.chaoxing.com'
driver.get(url)
driver.implicitly_wait(3)

driver.maximize_window()  # 这行代码可以把浏览器窗口最大化

driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys('')
driver.find_element(By.ID, 'pwd').send_keys('')
driver.find_element(By.CLASS_NAME, 'btn-big-blue.margin-btm24').click()  # 按登录键
driver.implicitly_wait(3)

driver.switch_to.frame('frame_content')  # 切换到“我学的课”这个frame

driver.find_elements(By.CLASS_NAME, 'course-name.overHidden2')[3].click()  # 点击进入“现代交换技术”课程 （一个class中有多个参数用“.”连接）
driver.implicitly_wait(3)

windows = driver.window_handles  # 获取所有窗口句柄  笔记：driver.current_window_handle --> 获取当前窗口句柄
driver.switch_to.window(windows[-1])  # 弹出了新窗口，所以切换到当前窗口（因为是新窗口，所以肯定是倒数第一个，所以index = -1）

driver.find_element(By.CLASS_NAME, 'zj').click()  # 进入“现代交换技术”后点击“章节”
driver.implicitly_wait(3)

driver.switch_to.frame('frame_content-zj')  # 进入“章节”这个frame
unit_select = driver.find_elements(By.CSS_SELECTOR, '[class="chapter_unit"]')[unit - 1]  # 选中第x章
unit_select.find_elements(By.CSS_SELECTOR, '[class="catalog_name"]')[lesson].click()  # 进入x章的第y课

# open_(address, '初始页面', driver.page_source)  # 获取当前网页源代码，与最后“返回命令”后的源代码作对比，做一个小实验

for frame_index in range(frames):
    driver.switch_to.frame('iframe')  # 进入此学习页面第一级frame
    # open_(address, '进入第一级', driver.page_source)  # 获取当前网页源代码

    iframe = driver.find_elements(By.TAG_NAME, 'iframe')[frame_index]  # 进入此学习页面第二级frame
    # open_(address, '进入第二级', driver.page_source)  # 获取当前网页源代码

    driver.switch_to.frame(iframe)  # iframe没有id或class时，可用标签或XPATH定位
    driver.switch_to.frame('frame_content')  # 进入此学习页面第三级frame
    # open_(address, '进入第三级', driver.page_source)  # 获取当前网页源代码

    au_url_list = driver.find_element(By.CLASS_NAME, 'swiper-wrapper').find_elements(By.CLASS_NAME, 'annex-audio')
    os.chdir(address + '\\' + str(frame_index + 1))
    for i in range(len(au_url_list)):
        au_url = au_url_list[i].find_element(By.TAG_NAME, 'audio').get_attribute('src')
        au_res = requests.get(au_url)
        with open('{}.mp3'.format(i + 1), 'wb') as f:
            f.write(au_res.content)

    driver.switch_to.default_content()  # 返回命令
    # open_(address, '返回命令后', driver.page_source)  # 获取当前网页源代码——实验证明：“返回命令后”不是返回到上一级frame，而是直接返回到初始页面
