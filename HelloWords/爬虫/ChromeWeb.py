from selenium import webdriver
import time, easygui

browser = webdriver.Chrome()

browser.get('http://www.baidu.com')

inputElement = browser.find_element_by_name('wd')
inputElement.clear()
inputElement.send_keys('12306')
inputElement.submit()

# easygui.msgbox('hehehe','title')
# code = easygui.textbox('验证信息','验证','')
# print(code)
# browser.quit()
