import time
import tkinter
import re
from tkinter import messagebox
from test01.provinces.mx.public_private_date import *
from test01.provinces.mx.importData import *




win = tkinter.Tk()
win.title("第一个程序")
win.geometry("500x100")

ll1 = tkinter.Label(win, text="开始日期:            ")
ll1.grid(row=0, column=0)
e1 = tkinter.Entry(win)
e1.grid(row=0, column=1)
lr1 = tkinter.Label(win, text="  日期格式为：2022-01-01            ")
lr1.grid(row=0, column=2)

ll2 = tkinter.Label(win, text="结束日期:            ")
ll2.grid(row=1, column=0)
e2 = tkinter.Entry(win)
e2.grid(row=1, column=1)
lr2 = tkinter.Label(win, text="  程序未开始！    ")
lr2.grid(row=1, column=2)

v1 = tkinter.IntVar()
btn1 = tkinter.Checkbutton(win, variable=v1, text="公有数据", bd=5)
btn1.grid(row=2, column=0)

v2 = tkinter.IntVar()
btn2 = tkinter.Checkbutton(win, variable=v2, text="私有数据", bd=5)
btn2.grid(row=2, column=1)



def check():
    if (e1.get() == "") or  (e2.get() == "") :

        messagebox.showinfo(title="警告",message="开始日期或结束日期为空")
        return False

    print(e1.get(),"   ",e2.get())

    r = re.compile('^20\d{2}-\d{2}-\d{2}$')
    if (r.match(e1.get()) is None) or (r.match(e2.get()) is None):
        messagebox.showinfo(title="警告",message="开始日期或结束日期格式错误")
        return False

    sd = datetime.datetime.strptime(e1.get(),"%Y-%m-%d")
    ed = datetime.datetime.strptime(e2.get(),"%Y-%m-%d")
    deviation = (ed-sd).days
    if deviation<0:
        messagebox.showinfo(title="警告",message="开始日期小于结束日期！！！")
        return False

    if (v1.get() == 0) and  (v2.get() ==0) :

        messagebox.showinfo(title="警告",message="请至少选中一种爬取的类型：公有数据或私有数据")
        return False

    return True

def exec():

    if  check() == False:

        return

    lr2.configure(text="正在爬取中...")
    win.update()
    b.configure(state=tkinter.DISABLED)

    type :int
    if (v1.get() == 1) and (v2.get() == 1):
        type = 0   #公有和私有
    elif v1.get() == 1:
        type = 1   #公有
    elif v2.get() == 1:
        type = 2   #私有

    print(type)

    seconds : int
    try:
        seconds = beginCrawl(e1.get(),e2.get(),type)

    except Exception:
        lr2.configure(text="程序发生错误...")
        b.configure(state=tkinter.ACTIVE)
        messagebox.showinfo(title="警告",message="请检查日期是否输入错误，或请联系管理员！")
        return

    t = "爬取结束，总共耗时: " + str(seconds) + " 秒！"
    lr2.configure(text=t)
    time.sleep(1)
    if type == 0 or type == 1:
        lr2.configure(text="正在导入在数据中心...")

        try:
            beginImport(e1.get(), e2.get())
        except Exception:
            lr2.configure(text="程序发生错误...")
            b.configure(state=tkinter.ACTIVE)
            messagebox.showinfo(title="警告", message="导入失败！！！")
            return

        lr2.configure(text="已成功导入到数据中心！！！")


    b.configure(state=tkinter.ACTIVE)


b = tkinter.Button(win,  text="点击开始", command=exec)
b.grid(row=3, column=1)

win.mainloop()