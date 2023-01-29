import time
import tkinter
import re
from datetime import datetime
from tkinter import messagebox
from provinces.mx.public_private_date import beginCrawl as mxCrawl
from provinces.mx.importData import beginImport as mxImport
from provinces.js.public_private_date import beginCrawl as jsCrawl
from provinces.js.importData import beginImport as jsImport
from provinces.ah.public_private_date import beginCrawl as ahCrawl
from provinces.ah.importData import beginImport as ahImport




win = tkinter.Tk()
win.title("第一个程序")
win.geometry("500x150")

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

needImport = tkinter.IntVar()
importBtn1 = tkinter.Checkbutton(win,text="是否需要导入到数据中心",variable=needImport)
importBtn1.grid(row=2, column=2)


radioBtn = tkinter.IntVar()
mxBtn1 = tkinter.Radiobutton(win,text="蒙西",value=0,variable=radioBtn)
jsBtn2 = tkinter.Radiobutton(win,text="江苏",value=1,variable=radioBtn)
ahBtn1 = tkinter.Radiobutton(win,text="安徽",value=2,variable=radioBtn)
mxBtn1.grid(row=3, column=0)
jsBtn2.grid(row=3, column=1)
ahBtn1.grid(row=3, column=2)
mxBtn1.select()



def check():
    if (e1.get() == "") or  (e2.get() == "") :

        messagebox.showinfo(title="警告",message="开始日期或结束日期为空")
        return False

    print(e1.get(),"   ",e2.get())

    r = re.compile('^20\d{2}-\d{2}-\d{2}$')
    if (r.match(e1.get()) is None) or (r.match(e2.get()) is None):
        messagebox.showinfo(title="警告",message="开始日期或结束日期格式错误")
        return False

    sd = datetime.strptime(e1.get(),"%Y-%m-%d")
    ed = datetime.strptime(e2.get(),"%Y-%m-%d")
    deviation = (ed-sd).days
    if deviation<0:
        messagebox.showinfo(title="警告",message="开始日期小于结束日期！！！")
        return False

    if (v1.get() == 0) and  (v2.get() ==0) :

        messagebox.showinfo(title="警告",message="请至少选中一种爬取的类型：公有数据或私有数据")
        return False

    if needImport.get() == 1 and v1.get()==0:
        messagebox.showinfo(title="警告", message='需要导入到数据中请勾选  "公有数据"')
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

    print(radioBtn.get())
    try:

        if radioBtn.get()== 0:
            seconds = mxCrawl(e1.get(),e2.get(),type)
        elif radioBtn.get()== 1:
            seconds = jsCrawl(e1.get(),e2.get(),type)
        elif radioBtn.get() == 2:
            seconds = ahCrawl(e1.get(), e2.get(), type)

    except Exception:
        lr2.configure(text="程序发生错误...")
        b.configure(state=tkinter.ACTIVE)
        messagebox.showinfo(title="警告",message="请检查日期是否输入错误，或请联系管理员！")
        return

    t = "爬取结束，总共耗时: " + str(seconds) + " 秒！"
    lr2.configure(text=t)
    lr2.update()
    time.sleep(1)

    if needImport.get()==1:
        lr2.configure(text="正在导入在数据中心...")
        lr2.update()
        try:

            if radioBtn.get() == 0:
                mxImport(e1.get(), e2.get())
            elif radioBtn.get() == 1:
                jsImport(e1.get(), e2.get())
            elif radioBtn.get() == 2:
                ahImport(e1.get(), e2.get())
        except Exception:
            lr2.configure(text="程序发生错误...")
            b.configure(state=tkinter.ACTIVE)
            messagebox.showinfo(title="警告", message="导入失败！！！")
            return

        lr2.configure(text="已成功导入到数据中心！！！")



    b.configure(state=tkinter.ACTIVE)


b = tkinter.Button(win,  text="点击开始", command=exec)
b.grid(row=4, column=1)

win.mainloop()