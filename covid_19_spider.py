import json
import os

import requests

from covidModel import CovidModel
from addCovidModel import AddCovidModel
from draw import Draw

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts'
response = requests.get(url=url)
responseJson = response.json()
data = json.loads(responseJson['data'])

# map函数 CovidModel是CovidModel初始化方法的简写
covidModels = map(CovidModel, data)

# 通过时间戳进行排序
covidModels = sorted(covidModels,key = lambda model:model.timeStamp)

#获取增加模型数组
addCovidModels = AddCovidModel.createAddCovidModels(covidModels = covidModels)

#获取日期和增加病例
dates, confirms = AddCovidModel.creatDatesAndConfirms(addCovidModels = addCovidModels)

#绘图
Draw.draw(dates, confirms)

# 当前工作目录 current working directory 
path = os.getcwd()

# 完成后打开文件夹
os.system(r"open {}".format(path))



