from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
desired_caps={}
desired_caps['platformName']='Android'

#模拟器设备
desired_caps['platformVersion']='4.4.2'
desired_caps['deviceName']='127.0.0.1:62001'

#mx4真机
# desired_caps['platformVersion']='5.1'
# desired_caps['deviceName']='MX4'
# desired_caps['udid']='750BBKL22GDN'

#desired_caps['app']=r'D:\tmp_downloads\com.tencent.mobileqq_7.6.8_872.apk'

desired_caps['appPackage']='com.tencent.mobileqq'
desired_caps['appActivity']='com.tencent.mobileqq.activity.SplashActivity'
desired_caps['noReset']='True'
desired_caps['unicodeKeyboard']="True"
desired_caps['resetKeyboard']="True"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

def check_longin():
	try:
		loginbtn=driver.find_element_by_id("com.tencent.mobileqq:id/btn_login")
	except NoSuchElementException:
		print("no loginbtn")
	else:
		loginbtn.click()
check_longin()
