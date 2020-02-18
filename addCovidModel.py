class AddCovidModel:
    def __init__(self, date, addConfirm, addSuspect, addDead, addHeal):
        """ Info的初始化方法 """
        self.date = date
        self.addConfirm = addConfirm
        self.addSuspect = addSuspect
        self.addDead = addDead
        self.addHeal = addHeal

    def modelInfo(self):
        print("时间: {}, 增加确诊: {}, 增加疑似: {}, 增加死亡: {}, 增加治愈: {}".format(self.date, self.addConfirm, self.addSuspect, self.addDead, self.addHeal))
        print("--------------------------------------------------------------")

    @staticmethod
    def createAddCovidModels(covidModels):
        addCovidModels = []

        for (index, model) in enumerate(covidModels, 1):

            if index == 1:
                #print("第一天")
                nextModel = covidModels[index]
                addInfo = AddCovidModel(nextModel.date, int(model.confirm), int(model.suspect), int(model.dead), int(model.heal))
                addCovidModels.append(addInfo)
            elif index == len(covidModels):
                #print("最后一天跳出循环")
                break
            else:
                nextModel = covidModels[index]
                date = nextModel.date
                addConfirm = int(nextModel.confirm) - int(model.confirm)
                addSuspect = int(nextModel.suspect) - int(model.suspect)
                addDead = int(nextModel.dead) - int(model.dead)
                addHeal = int(nextModel.heal) - int(model.heal)
                addInfo = AddCovidModel(date, addConfirm, addSuspect, addDead, addHeal)
                addCovidModels.append(addInfo)

        return addCovidModels

    @staticmethod
    def creatDatesAndConfirms(addCovidModels):
        dates = map(lambda addCovidModel: addCovidModel.date, addCovidModels)
        confirms = map(lambda addCovidModel: addCovidModel.addConfirm, addCovidModels)
        return (list(dates), list(confirms))