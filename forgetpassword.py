from tkinter import*
import pymysql
import pymysql.cursors
import os
from tkinter import messagebox
from PIL import ImageTk, Image

win=Tk()
win.geometry("400x400")
win.title("Forget Password Page")
win.resizable(False,False)
load=Image.open('fo.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)


def insert():
    a=str(num1.get())
    b=str(num2.get())
    c=str(num3.get())
    conn = pymysql.connect(host='localhost',user='root',password='123456',db='mad')
    mydb=conn.cursor()
    mydb.execute("select password from login where username='"+c+"'")
    conn.commit()
    result=mydb.fetchall()
    count=mydb.rowcount
    print(result)
    print(count)
    if count>0:
        for row in result:
            {
                messagebox.showinfo("Message",row)
            }
    else:
        messagebox.showerror("Message","Fill Details")
  
frame=Frame(win,bd=10,relief="raised",width=400,height=50).grid(row=0)
lb=Label(frame,font=('arial',15,'bold'),text="FORGET PASSWORD").grid(row=0)

lb=Label(win,font=('arial',10,'bold'),text="First Name",width=16).place(x=20,y=100)
lb2=Label(win,font=('arial',10,'bold'),text="Last Name",width=16).place(x=20,y=150)
lb3=Label(win,font=('arial',10,'bold'),text="User Name",width=16).place(x=20,y=200)

num1=StringVar()
tx=Entry(win,width=30,textvariable=num1).place(x=180,y=100)
num2=StringVar()
tx2=Entry(win,width=30,textvariable=num2).place(x=180,y=150)
num3=StringVar()
tx3=Entry(win,width=30,textvariable=num3).place(x=180,y=200)

btn=Button(win,text="Submit",font=('arial',10,'bold'),command=insert,width=15,bd=8,relief="raised").place(x=130,y=280)
win.mainloop()
