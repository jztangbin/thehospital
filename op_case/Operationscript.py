import utils.op_excel



class steps(object):
    def tablerevise(self):  #循环处理数据
        for i in range(2,utils.op_excel.sheet.max_row+1):
            utils.op_excel.exceloperate().updatedata(i,2)







if __name__ == "__main__":
    steps().tablerevise()

