#coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
#image=Image.open("S:/code2.png")
#text=pytesseract.image_to_string(image)
#print(text)

r = ShowapiRequest("http://route.showapi.com/184-4","88961","5111a719c3eb4df29604dec28cbe1e47" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"S:/code2.png") #文件上传时设置
res = r.post()
text=res.json()['showapi_res_body']['Result']
print(text) # 返回信息