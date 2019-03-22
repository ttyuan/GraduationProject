#coding=utf-8
from selenium import webdriver
import time
import random
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.by import By 
#driver = webdriver.Chrome()
driver = webdriver.Edge()
#driver = webdriver.Firefox()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))
#判断元素是否显示出来
#element=driver.find_element_by_class_name("controls")

email_element=driver.find_element_by_id("register_email")
#处理验证码
driver.save_screenshot("S:\GraduationProject\img\code2.png")
code_element=driver.find_element_by_id("getcode_num")
#code_element.location
left=code_element.location['x']
top=code_element.location['y']
right=code_element.size['width']+left
height=code_element.size['height']+top
im=Image.open("S:\GraduationProject\img\code2.png")
#img=im.crop((left,top,right,height))
#img.save("S:/code1.png")
#分辨率问题
#获取窗口可视范围的width和height
html = driver.find_element_by_tag_name("html")
#设置图片重新打开的width和height
resize_width = html.size['width']
resize_height = html.size['height']
#resize图片
resize_img = im.resize((resize_width, resize_height), Image.BILINEAR)
img = resize_img.crop((left, top, right, height))
img.save("S:\GraduationProject\img\code3.png")
r = ShowapiRequest("http://route.showapi.com/184-4","88961","5111a719c3eb4df29604dec28cbe1e47" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"S:\GraduationProject\img\code3.png") #文件上传时设置
res = r.post()
text=res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(2)
driver.find_element_by_id("captcha_code").send_keys(text)#输入验证码

#生成用户名(随机)
for i in range(5):
    user_email=''.join(random.sample('1234567890abcdefg',5))+"@163.com"


#定位
#locator=(By.CLASS_NAME,"controls")
#EC.visibility_of_element_located(element)
#WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))

#获取属性
email_element=driver.find_element_by_id("register_email")
print(email_element.get_attribute("placeholder"))
email_element.send_keys("test@163.com")
print(email_element.get_attribute("value"))
time.sleep(5)
driver.close()

#driver.find_element_by_id("register_email").send_keys("mushishi_01@163.com")
#user_name_element_node = driver.find_elements_by_class_name("controls")[1]
#user_element = user_name_element_node.find_element_by_class_name("form-control")
#user_element.send_keys("mushishi01")
#driver.find_element_by_name("password").send_keys("111111")
#driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("1111")
