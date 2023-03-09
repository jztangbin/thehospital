import datetime
from copy import copy
import datetime
from time import strftime
import openpyxl
import yaml
import time



f = open('F://work//theHospital//theConfig.yaml')
data = yaml.load(f.read(),Loader=yaml.FullLoader)  #读配置
wb = openpyxl.load_workbook(data['excel']['local'])  #实例化
newwb = copy(wb)
sheet = newwb.active
savetime = datetime.datetime.now()


class exceloperate(object):  #获取身份证
    def getcarnumber(self,row):
        return sheet.cell(row,4).value

    def updatedata(self,row,key):  #新建表格存储数据
        try:
            sheet['E'+str(row)] = key
            newwb.save(data['excel']['sqvelocal']+"Rankingfilter"+savetime.strftime("%Y-%m-%d")+".xlsx")
        finally:
            newwb.close()
        return print(sheet.cell(row,3).value,"的数据更新为",sheet.cell(row,5).value)

if  __name__ =='__main__':
    exceloperate().updatedata(2,3)
