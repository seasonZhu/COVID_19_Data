import requests
import json

""" 这是原始思路 """

class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__
 
def dict_to_object(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    inst=Dict()
    for k,v in dictObj.items():
        inst[k] = dict_to_object(v)
    return inst

import datetime
import time

class Info:
    """ 信息模型 """
    """ 
    {
    'confirm': '440', 
    'confirm_cuts': None, 
    'date': '01/21', 
    'dead': '9', 
    'dead_cuts': None, 
    'heal': '25', 
    'heal_cuts': None, 
    'now_confrim': None, 
    'now_confrim_cuts': None, 
    'now_severe': None, 
    'now_severe_cuts': None, 
    'suspect': '37', 
    'suspect_cuts': None
    }
     """
    def __init__(self, dictionary):
        """ Info的初始化方法 """
        self.date = dictionary['date']
        self.timeStamp = self.getTimeStamp(date = self.date)
        self.confirm = dictionary['confirm']
        self.suspect = dictionary['suspect']
        self.dead = dictionary['dead']
        self.heal = dictionary['heal']

    def getTimeStamp(self, date):
        realDate = "2019/" + date
        timeArray = time.strptime(realDate, "%Y/%m/%d")
        timeStamp = time.mktime(timeArray)
        #print(timeStamp)
        return timeStamp

    def printInfo(self):
        print("时间: {}, 确诊: {}, 疑似: {}, 死亡: {}, 治愈: {}".format(self.date, self.confirm, self.suspect, self.dead, self.heal))
        print("--------------------------------------------------------------")

class AddInfo:
    def __init__(self, date, addConfirm, addSuspect, addDead, addHeal):
        """ Info的初始化方法 """
        self.date = date
        self.addConfirm = addConfirm
        self.addSuspect = addSuspect
        self.addDead = addDead
        self.addHeal = addHeal

    def printInfo(self):
        print("时间: {}, 增加确诊: {}, 增加疑似: {}, 增加死亡: {}, 增加治愈: {}".format(self.date, self.addConfirm, self.addSuspect, self.addDead, self.addHeal))
        print("--------------------------------------------------------------")


url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts'
response = requests.get(url=url)
jsonDict = response.json()
jsonArray = json.loads(jsonDict['data'])

infoArray = []

for dictionary in jsonArray:
    model = Info(dictionary = dictionary)
    infoArray.append(model)

# 通过时间戳进行排序
infoArray = sorted(infoArray,key = lambda model:model.timeStamp)

addInfoArray = []

# index从1开始
for (index, info) in enumerate(infoArray, 1):
    #print(index)
    #print(info.timeStamp)
    #print(info.printInfo())

    if index == 1:
        #print("第一天")
        addInfo = AddInfo(model.date, model.confirm, model.suspect, model.dead, model.heal)
        addInfoArray.append(addInfo)
    elif index == len(infoArray):
        #print("最后一天跳出循环")
        break
    else:
        nextInfo = infoArray[index]
        date = nextInfo.date
        addConfirm = int(nextInfo.confirm) - int(info.confirm)
        addSuspect = int(nextInfo.suspect) - int(info.suspect)
        addDead = int(nextInfo.dead) - int(info.dead)
        addHeal = int(nextInfo.heal) - int(info.heal)
        addInfo = AddInfo(date, addConfirm, addSuspect, addDead, addHeal)
        addInfoArray.append(addInfo)

addInfoArray = addInfoArray[1: -1]

dates = []
addConfirms = []
addSuspects = []
for addInfo in addInfoArray:
    print(addInfo.__dict__)
    dates.append(addInfo.date)
    addConfirms.append(addInfo.addConfirm)
    addSuspects.append(addInfo.addSuspect)

# import matplotlib.pyplot as plt

# plt.plot(dates, addConfirms, linewidth=5)

# plt.title("Confirm of Every Day", fontsize=24) 
# plt.xlabel("Date", fontsize=3)
# plt.ylabel("Confirm", fontsize=14) # 设置刻度标记的大小
# #plt.tick_params(axis='both', labelsize=14) 
# plt.show()

import pygal


my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False

#以下三句设置字体的语句有问题
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18

my_config.truncate_label = 15 # 将标签截断为15个字符
                              # 如果将鼠标指向被截断的标签，将显示完整标签
my_config.show_y_guides = True # 隐藏图表中的水平线（y guide lines）
my_config.width = 1000 # 图标宽度，默认800

hist = pygal.Bar(my_config)
hist.title = "每日确诊数量" 
hist.x_labels = dates
hist.x_title = "日期"
hist.y_title = "确诊"
hist.add('当日确诊数', addConfirms) 
hist.render_to_file('Confirm of Every Day.svg')

# histSuspects = pygal.Bar(my_config)
# histSuspects.title = "每日疑似数量" 
# histSuspects.x_labels = dates
# histSuspects.x_title = "日期"
# histSuspects.y_title = "疑似"
# histSuspects.add('今天疑似数', addSuspects) 
# histSuspects.render_to_file('Suspect of Every Day.svg')