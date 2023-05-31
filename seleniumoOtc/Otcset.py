from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
import openpyxl
from utils import op_excel
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



# url地址
url = 'http://172.17.149.242:9010/#/login?redirect=%2F'

# 定义chrome驱动去地址
path = Service('chromedriver.exe')

# 创建浏览器操作对象
browser = webdriver.Chrome(service=path)


browser.get(url)
sleep(40)
iframe = browser.find_element(By.XPATH,value='//*[@id="hgs-b02-b17-01"]')
browser.switch_to.frame(iframe)
btn = browser.find_element(By.XPATH,value='//*[@id="app"]/div/section/div/section[1]/div/div[2]/div/div/div[2]/div/div[1]')
ActionChains(browser).move_to_element(btn).perform()
sleep(2)
btn1 = browser.find_element(By.XPATH,value='//*[@id="app"]/div/section/div/section[1]/div/div[2]/div/div/div[2]/div/div[3]/a')
btn1.click()
sleep(5)
btn2 = browser.find_element(By.XPATH,value='/html/body//div[2]//div//div[2]/div[2]/div[2]/div/form/div/div[1]/div/div/div/div/span/div[2]/div/input')
btn3 = browser.find_element(By.XPATH,value='/html/body/div[2]/div//div[3]/span/span/button[3]')
for i in range(2,op_excel.resheet.max_row+1):
    print(op_excel.resheet.max_row)
    print(i)
    carnumb = op_excel.exceloperate().reportcarnum(i)
    print(carnumb)
    try:
        btn2.click()
        btn2.send_keys(carnumb)
        btn2.send_keys(Keys.ENTER)
        sleep(5)
        # cframe = browser.find_element(By.XPATH,value='//*[@id="hgs-b02-b17-01"]')
        # browser.switch_to.frame(cframe)
        btn3.click()
        sleep(3)
        btn2.clear()
        sleep(10)
    except:
        ActionChains(browser).move_to_element(btn).perform()
        sleep(2)
        btn1.click()
        sleep(5)

browser.quit()







