#coding=utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time
class GetCode:
    def __init__(self,driver):
        self.driver = driver

    #获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element=self.driver.find_element_by_id("getcode_num")
        left=code_element.location['x']
        top=code_element.location['y']
        right=code_element.size['width']+left
        height=code_element.size['height']+top
        im=Image.open(file_name)
        #分辨率问题
        #获取窗口可视范围的width和height
        html = self.driver.find_element_by_tag_name("html")
        #设置图片重新打开的width和height
        resize_width = html.size['width']
        resize_height = html.size['height']
        #resize图片
        resize_img = im.resize((resize_width, resize_height), Image.BILINEAR)
        img = resize_img.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(2)

    #解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4","88961","5111a719c3eb4df29604dec28cbe1e47" )
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name) #文件上传时设置
        res = r.post()
        text=res.json()['showapi_res_body']['Result']
        time.sleep(2)
        return text
        #code = text['Result']
        
        #return code