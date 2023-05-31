import time

from utils import op_excel
from base import requestHP
from random import randint
from time import sleep

class steps(object):
    def tablerevise(self):  #循环处理数据
        for i in range(2,op_excel.sheet.max_row+1):
            print(op_excel.sheet.max_row)
            waittime = randint(1,2)
            sleep(waittime)
            print(i)
            carnumb = op_excel.exceloperate().getcarnumber(i)
            try:
                respones = requestHP.requestgather().getinsutypeinfo(carnumb).json()
            except:
                print(i)
            if respones['data']['data'] != []:
                print(respones['data']['data'][0]['insutype'])
                if respones['data']['data'][0]['insutype'] == '310':
                    key = 1 #职工医疗
                    print(key)
                elif respones['data']['data'][0]['insutype'] == '390':
                    key = 2  #城乡医疗
                elif respones['data']['data'][0]['insutype'] == None:
                    key = 0
                    print(key)
            else:key = 'f'
            op_excel.exceloperate().updatedata(i,key)
        op_excel.newwb.save(op_excel.data['excel']['sqvelocal'] + "Rankingfilter" + op_excel.savetime.strftime("%Y-%m-%d") + ".xlsx")


    def updatetable(self):
        for i in range(2,op_excel.sheet.max_row+1):
            carnumb = op_excel.exceloperate().getcarnumber(i)
            try:
               respones = requestHP.requestgather().updatecarnumber(carnumb)
               print(respones.json())
            except:
                print(i)

    # def  saveHpinfo(self):
    #     for i in range(2,op_excel.resheet.max_row+1):
    #         carnumb = op_excel.exceloperate().reportcarnum(i)
    #         print(carnumb)
    #         cominforespones = requestHP.requestgather().getinsutypeinfo(carnumb).json()
    #         insuinforespones = requestHP.requestgather().getupdateinfo(cominforespones['data']['data'][0]['psnNo']).json()
    #         psnNo = insuinforespones['data'][0]['psnNo']
    #         brdy = cominforespones['data']['data'][0]['brdy']
    #         insutype = cominforespones['data']['data'][0]['insutype']
    #         insuAdmdvs = insuinforespones['data'][0]['insuAdmdvs']
    #         psnInsuRltsId = insuinforespones['data'][0]['psnInsuRltsId']
    #         psnName = cominforespones['data']['data'][0]['psnName']
    #         certno = insuinforespones['data'][0]['certno']
    #         psnCertType = cominforespones['data']['data'][0]['psnCertType']
    #         gend = insuinforespones['data'][0]['gend']
    #         naty = insuinforespones['data'][0]['naty']
    #         psnType = cominforespones['data']['data'][0]['psnType']
    #         tel = cominforespones['data']['data'][0]['tel']
    #         empName = cominforespones['data']['data'][0]['empName']
    #         empNo = cominforespones['data']['data'][0]['empNo']
    #         addr = cominforespones['data']['data'][0]['liveAddr']
    #         psnTypeName = insuinforespones['data'][0]['psnTypeName']
    #         insutypeName = insuinforespones['data'][0]['insutypeName']
    #         natyName = insuinforespones['data'][0]['natyName']
    #         gendName = insuinforespones['data'][0]['gendName']
    #         admdvsName = insuinforespones['data'][0]['admdvsName']
    #         liveAddr = cominforespones['data']['data'][0]['liveAddr']
    #         age = cominforespones['data']['data'][0]['age']
    #         memo = cominforespones['data']['data'][0]['memo']
    #         data = '{"psnNo":"' +psnNo+ '","brdy":"'+brdy+'","dclaSouc":"01","insutype":"'+insutype+'","insuAdmdvs":"'+insuAdmdvs+'","psnInsuRltsId":"'+psnInsuRltsId+'","psnName":"'+psnName+'","certno":"'+str(certno)+'","psnCertType":"'+psnCertType+'","gend":"'+gend+'","naty":"'+naty+'","psnType":"'+psnType+'","tel":"'+tel+'","empName":"'+empName+'","empNo":"'+empNo+'","addr":"'+addr+'","psnTypeName":"'+psnTypeName+'","insutypeName":"'+insutypeName+'","natyName":"'+natyName+'","gendName":"'+gendName+'","admdvsName":"'+admdvsName+'","liveAddr":"'+liveAddr+'","age":"'+age+'","medTrtType":"110","dateRange":["2023-01-01","2023-12-31"],"memo":"","planMatnDate":"","begndate":"2023-01-01","enddate":"2023-12-31","agnterName":"","agnterCertType":"","agnterCertno":"","agnterTel":"","agnterRlts":"","agnterAddr":"","psnFixRegDetlEvtDTOList":[{"fixmedinsCode":"H44011100732","fixmedinsName":"白云区棠景街第一社区卫生服务中心","begndate":"2023-01-01","enddate":"2023-12-31"}],"wflwCode":"HGS060","nodeCode":"HGS06001","tcmFlag":"0","fixmedinsCode":"H44011100732","fixmedinsName":"白云区棠景街第一社区卫生服务中心","bizAcpId":"MZGD11202303162060","subFlag":"2"}'
    #         print(data)
    #         #respones = requestHP.requestgather().updatecarnumber(data)
    #         #print(respones.json())
    #         print(i)
    #
    #
    #
    #
    #
    #
    #
    #
    #

if __name__ == "__main__":
    #steps().saveHpinfo()
    steps().tablerevise()

