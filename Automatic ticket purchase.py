import random
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service  # 导入 Service 类
from selenium.webdriver.common.by import By

zh = '18888888888'
mm = '123456'  # TODO password
sfz_id = '5555'  # TODO id_card[-1:-4]
fs = '上海西'  # TODO from_station
ts = '北京东'  # TODO to_station
Time = '2023-04-06'  # TODO date
url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E4%B8%8A%E6%B5%B7,SHH&date=2025-04-18&flag=N,N,Y'

# 创建 Service 实例并传递 chromedriver 路径
service = Service(executable_path=r"E:\python3.11.9\chromedriver.exe")

# 使用 service 参数创建 Chrome WebDriver
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get(url=url)

# 最大化窗口
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(10)
# 使用 CSS_SELECTOR 查找元素并进行操作
driver.find_element(By.CSS_SELECTOR, '#fromStationText').clear()
driver.find_element(By.CSS_SELECTOR, '#fromStationText').send_keys(fs + Keys.RETURN)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#toStationText').clear()
driver.find_element(By.CSS_SELECTOR, '#toStationText').send_keys(ts + Keys.RETURN)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#train_date').clear()
driver.find_element(By.CSS_SELECTOR, '#train_date').send_keys(Time + Keys.RETURN)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#query_ticket').click()

driver.find_element(By.CSS_SELECTOR, '#queryLeftTable tr:nth-child(7) .btn72').click()  # TODO 预定座位
time.sleep(1)
"""登录"""
driver.find_element(By.CSS_SELECTOR, '#J-userName').send_keys(zh)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#J-password').send_keys(mm)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#J-login').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#id_card').send_keys(sfz_id)
driver.find_element(By.CSS_SELECTOR, '#verification_code').click()  # TODO 获取验证码
code = input('请输入验证码:')
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, '#code').send_keys(code)  # TODO 登录账号
driver.find_element(By.CSS_SELECTOR, '#sureClick').click()
time.sleep(random.random())

driver.find_element(By.CSS_SELECTOR, '#normalPassenger_0').click()  # TODO 选择乘车人
time.sleep(random.random())
# driver.find_element(By.CSS_SELECTOR, '#dialog_xsertcj_cancel').click()  # TODO 确认是否学生票(取消)
# time.sleep(random.random())
driver.find_element(By.CSS_SELECTOR, '#dialog_xsertcj_ok').click()  # TODO 确认是否学生票(确认)
time.sleep(random.random())
driver.find_element(By.CSS_SELECTOR, '#submitOrder_id').click()  # TODO 提交订单
time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, '#qd_closeDefaultWarningWindowDialog_id').click()  # TODO 学生票用
# time.sleep(random.random())
# driver.find_element(By.CSS_SELECTOR, '#1D').click()  # TODO 选择座位
# time.sleep(random.random())
driver.find_element(By.CSS_SELECTOR, '#qr_submit_id').click()  # TODO 确定座位
time.sleep(15)
driver.find_element(By.CSS_SELECTOR, '#conf_xspnalert').click()  # TODO 确认学生票
time.sleep(random.random())
driver.find_element(By.CSS_SELECTOR, '#payButton').click()  # TODO 开始支付
time.sleep(random.random())
driver.find_element(By.CSS_SELECTOR, '#continuePay').click()  # TODO 是否购买铁路险
# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]/div/form/div[10]').click()  # TODO 选择支付方式,微信支付
time.sleep(500)
