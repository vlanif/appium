from find_element.start import driver,NoSuchElementException
def login():
   try:
       driver.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]').clear()
       driver.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]').send_keys('273659024')
       driver.find_element_by_xpath('//android.widget.EditText[@content-desc="密码 安全"]').send_keys('...')
       driver.find_element_by_id('com.tencent.mobileqq:id/login').click()
   except NoSuchElementException:
       print("yijing login")
   else:
       login()
driver.implicitly_wait(5)
def sendmess():
    try:
        driver.find_element_by_id('com.tencent.mobileqq:id/title').click()
        #driver.find_element_by_id('com.tencent.mobileqq:id/input').send.keys("我是机器人")
    except NoSuchElementException:
        print("no huihua")
    else:
        sendmess()

