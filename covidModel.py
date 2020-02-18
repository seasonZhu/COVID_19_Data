import time

class CovidModel:
    """ 模型 """
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
        """ 初始化方法 """
        self.date = dictionary['date']
        self.timeStamp = self.getTimeStamp(date = self.date)
        self.confirm = dictionary['confirm']
        self.suspect = dictionary['suspect']
        self.dead = dictionary['dead']
        self.heal = dictionary['heal']

    def getTimeStamp(self, date):
        realDate = "2020/" + date
        timeArray = time.strptime(realDate, "%Y/%m/%d")
        timeStamp = time.mktime(timeArray)
        #print(timeStamp)
        return timeStamp

    def modelInfo(self):
        print("时间: {}, 确诊: {}, 疑似: {}, 死亡: {}, 治愈: {}".format(self.date, self.confirm, self.suspect, self.dead, self.heal))
        print("--------------------------------------------------------------")