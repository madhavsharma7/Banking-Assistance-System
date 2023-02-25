from tkinter import*
import pymysql
import pymysql.cursors
from tkinter import messagebox
from PIL import ImageTk, Image

win=Tk()
win.geometry("500x500")
win.resizable(False,False)
win.title("Welcome to the Contact Page")
load=Image.open('si.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
img.place(x=0,y=0)

def update():
    a=str(num.get())
    b=str(num1.get())
    c=str(num2.get())
    d=str(num3.get())
    e=str(num4.get())

    try:
        if(e==d):
            conn = pymysql.connect(host='localhost',user='root',password='123456',db='mad')
            mydb=conn.cursor()
            mydb.execute("update depos set contact='"+d+"' where contact='"+c+"'")
            conn.commit()
            messagebox.showinfo("Message","Contact Updated")
        else:
            messagebox.showinfo("Message","Not Match")
    except:
        conn.rollback()
        print("Not Changed")
    conn.close()

lb=Label(win,text="Enter Card Number ",font=20,width=20).grid(row=0,column=0,padx=20,pady=20)

lb2=Label(win,text="Enter Pin",font=20,width=10).grid(row=1,column=0,padx=20,pady=20)

lb3=Label(win,text="Enter Old Contact_No.",font=20,width=17).grid(row=2,column=0,padx=20,pady=20)

lb4=Label(win,text="Enter New Contact_No.",font=20,width=20).grid(row=3,column=0,padx=20,pady=20)

lb5=Label(win,text="Re_Enter the Contact_No.",font=20,width=20).grid(row=4,column=0,padx=20,pady=20)

num=StringVar()
tx=Entry(win,font=10,width=20,textvariable=num).grid(row=0,column=1)
num1=StringVar()
tx2=Entry(win,font=10,width=20,textvariable=num1).grid(row=1,column=1)
num2=StringVar()
tx3=Entry(win,font=10,width=20,textvariable=num2).grid(row=2,column=1)
num3=StringVar()
tx4=Entry(win,font=10,width=20,textvariable=num3).grid(row=3,column=1)
num4=StringVar()
tx5=Entry(win,font=10,width=20,textvariable=num4).grid(row=4,column=1)

btn=Button(win,command=update,text="Update",relief="raised",bd=10,font=20,highlightbackground="blue",highlightthickness=10).place(x=200,y=370)

win.mainloop()
