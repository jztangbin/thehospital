import requests
import json

X = 'X'


class requestgather(object):
    header = {'Content-Type': 'application/json;charset=UTF-8',
              'Cookie':'XSRF-TOKEN=eca8bbf4-56ba-46b3-a900-c6201fecd635; SESSION=ZGNjMjI0MmMtNGFiZS00ZDQzLWI5MmMtNTk5Y2EyNzAyZWIx; sidebarStatus=0',
              'X-XSRF-TOKEN': 'eca8bbf4-56ba-46b3-a900-c6201fecd635'}
    # reportheader = {'Content-Type': 'application/json;charset=UTF-8',
    #           'Cookie': 'XSRF-TOKEN=e9210a24-7135-44c4-9de2-2a1c8cafb68f; SESSION=ZDg0YTQ3NWYtMWMxOS00MzBkLTg2NTYtNTU2Y2M0OWIxMTBh; sidebarStatus=0',
    #           'X-XSRF-TOKEN': 'e9210a24-7135-44c4-9de2-2a1c8cafb68f'}
    def getinsutypeinfo(self, carnum):#获取用户信息
        url = 'http://172.17.149.242:9010/hsa-mbs-nes-4401/web/mba/inc/combizmgt/comQuery/queryPsnComInfo'
        headers = requestgather().header
        datas = '{"queryContent":"' + str(carnum) + '","pageSize":10,"pageNum":1}'
        respones = requests.post(url, data=datas, headers=headers)
        print(respones.json())
        return respones

    def getupdateinfo(self,carnum):#获取用户信息
        url = 'http://172.17.149.242:9010/hsa-mbs-nes-4401/web/mba/inc/combizmgt/comQuery/queryPsnInsuInfo'
        headers = requestgather().header
        datas = '{"psnNo":"' + str(carnum) + '","queryPsnFilter":"1,2"}'
        respones = requests.post(url,data=datas, headers=headers)
        print(respones.json())
        return respones

    # def updatecarnumber(self,data):#提交保存
    #     url = 'http://172.17.149.242:9010/hsa-hgs-4401/web/ihs/mdt/psntrtdclamgt/psnfix/insertPsnFixApplyInfo'
    #     headers = requestgather.header
    #     datas = data
    #     respones = requests.post(url,headers=headers,data=datas.encode())
    #     print(respones.json())
    #     return respones


if __name__ == '__main__':
    requestgather().getinsutypeinfo('41302519690211153X')
