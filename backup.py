# encoding=utf8

from appium import webdriver
from selenium.webdriver.common.by import By

#手机的连接配置信息写入字典中
desired_caps={
  "platformName": "Android",
  "deviceName": "Quest 2",
  "platformVersion": "10"
}
#调用webdriver模块中的Remote方法启动APP
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element(By.ID, "com.android.backupconfirm:id/button_allow").click()
