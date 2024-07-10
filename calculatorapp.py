import tkinter as tk
window=tk.Tk()
window.title("SIMPLE CALCULATOR")

entry=tk.Entry(master=window,borderwidth=2,width=50)
entry.grid(row=0,column=0,columnspan=5,ipadx=10,ipady=10,padx=5)

#funtion
def equal():
    try:
        s_num=entry.get()
        s_num=int(s_num)
        entry.delete(0,tk.END)
        if(math=="add"):
            entry.insert(0,f_num+s_num)
        if(math=="sub"):
            entry.insert(0,f_num-s_num)
        if(math=="mul"):
            entry.insert(0,f_num*s_num)
        if(math=="div"):
            try:
                entry.insert(0,f_num/s_num)
            except ZeroDivisionError:
                entry.insert(0,"invalid input")
        if(math=="exp"):
            entry.insert(0,f_num**s_num)
    except ValueError:
        entry.delete(0,tk.END)
    
def clear():
    entry.delete(0,tk.END)
def click(num):
    n1=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,str(n1)+str(num))
def add():
    try:
        first_num=entry.get()
        entry.delete(0,tk.END)
        global f_num
        global math
        math="add"
        f_num=int(first_num)
    except ValueError:
        entry.insert(0,"invalid input")
def sub():
    try:
        first_num=entry.get()
        entry.delete(0,tk.END)
        global f_num
        global math
        math="sub"
        f_num=int(first_num)
    except ValueError:
        entry.insert(0,"invalid input")
def mul():
    try:
        first_num=entry.get()
        entry.delete(0,tk.END)
        global f_num
        global math
        math="mul"
        f_num=int(first_num)
    except ValueError:
        entry.insert(0,"invalid input")
def div():
    try:
        first_num=entry.get()
        entry.delete(0,tk.END)
        global f_num
        global math
        math="div"
        f_num=int(first_num)
    except ValueError:
        entry.insert(0,"invalid input")
def exp():
    try:
        first_num=entry.get()
        entry.delete(0,tk.END)
        global f_num
        global math
        math="exp"
        f_num=int(first_num)
    except ValueError:
        entry.insert(0,"invalid input")
#buttons
btn_7=tk.Button(window,text="7",width=5,height=2,command=lambda:click(7))
btn_7.grid(row=1,column=0,ipadx=5,ipady=5,padx=20,pady=5)
btn_8=tk.Button(window,text="8",width=5,height=2,command=lambda:click(8))
btn_8.grid(row=1,column=1,ipadx=5,ipady=5)
btn_9=tk.Button(window,text="9",width=5,height=2,command=lambda:click(9))
btn_9.grid(row=1,column=2,ipadx=5,ipady=5,padx=20)

btn_4=tk.Button(window,text="4",width=5,height=2,command=lambda:click(4))
btn_4.grid(row=2,column=0,ipadx=5,ipady=5,padx=20)
btn_5=tk.Button(window,text="5",width=5,height=2,command=lambda:click(5))
btn_5.grid(row=2,column=1,ipadx=5,ipady=5)
btn_6=tk.Button(window,text="6",width=5,height=2,command=lambda:click(6))
btn_6.grid(row=2,column=2,ipadx=5,ipady=5,padx=20)

btn_1=tk.Button(window,text="1",width=5,height=2,command=lambda:click(1))
btn_1.grid(row=3,column=0,ipadx=5,ipady=5,padx=20)
btn_2=tk.Button(window,text="2",width=5,height=2,command=lambda:click(2))
btn_2.grid(row=3,column=1,ipadx=5,ipady=5)
btn_3=tk.Button(window,text="3",width=5,height=2,command=lambda:click(3))
btn_3.grid(row=3,column=2,ipadx=5,ipady=5)
btn_0=tk.Button(window,text="0",width=5,height=2,command=lambda:click(0))
btn_0.grid(row=4,column=1,ipadx=5,ipady=5)

btn_multi=tk.Button(window,text="x",width=5,height=2,command=mul)
btn_multi.grid(row=1,column=3,ipadx=5,ipady=5)
btn_sub=tk.Button(window,text="-",width=5,height=2,command=sub)
btn_sub.grid(row=2,column=3,ipadx=5,ipady=5)
btn_add=tk.Button(window,text="+",width=5,height=2,command=add)
btn_add.grid(row=3,column=3,ipadx=5,ipady=5)
btn_div=tk.Button(window,text="/",width=5,height=2,command=div)
btn_div.grid(row=4,column=2,ipadx=5,ipady=5)
btn_exp=tk.Button(window,text="^",width=5,height=2,command=exp)
btn_exp.grid(row=4,column=0,ipadx=5,ipady=5)


btn_clear=tk.Button(window,text="C",width=5,height=2,command=clear)
btn_clear.grid(row=4,column=3,ipadx=5,ipady=5)
btn_equal=tk.Button(window,text="=",width=39,height=2,command=equal)
btn_equal.grid(row=5,column=0,ipadx=5,ipady=5,columnspan=5)

window.mainloop()