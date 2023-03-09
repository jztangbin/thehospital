import tkinter as tk
from tkinter import messagebox
from tkinter import *
import op_case.Operationscript

root = tk.Tk()
root.title('hpOperation')
root.geometry('400x300+630+80')

lable1 = Label(root,text = "批量处理医保信息",padx=40,pady=0,font=20)
lable1.pack(side=LEFT,anchor=NW,pady=10,padx=10)
btn1 = tk.Button(root,text='确定',padx=40,pady=0)
btn1.pack(side=LEFT,anchor=NE,pady=10,padx=10)
lable2 = Label(root,text = "批量处理医保信息",padx=40,pady=60,font=20)
lable2.pack(side=LEFT,pady=10,padx=10)
btn2 = tk.Button(root,text='确定',padx=40,pady=60)
btn2.pack(side=LEFT,pady=10,padx=10)


def testbox(e):
    if messagebox.askquestion("点击确定开始批量处理", "批量处理中请勿关闭主窗口") == "yes":
        op_case.Operationscript.steps().tablerevise()
        messagebox.showinfo("","批量处理已完成")
    else:
        return


btn1.bind("<Button-1>",testbox)
root.mainloop()







