from tkinter import *
from tkinter.messagebox import*
root=Tk()
root.geometry('1500x1500')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=(1000//3))
Label(root,text="Online Bus Booking System",font='Cambria 20 bold',fg='Red',bg='LightBlue1').grid(row=1,column=0,columnspan=10)
Label(root,text="ENTER JOURNEY DETAILS",font='Cambria 15 bold',fg='ForestGreen',bg='PaleGreen').grid(row=2,column=0,columnspan=10,pady=(1000//100))
Label(root,text="To:",font='Cambria 10',fg='Black').grid(row=3,column=0)
Entry(root).grid(row=3,column=1)
Label(root,text="From:",font='Cambria 10',fg='Black').grid(row=3,column=2)
Entry(root).grid(row=3,column=3)
Label(root,text="Journey date:",font='Cambria 10',fg='Black').grid(row=3,column=4)
Entry(root).grid(row=3,column=5)
def fun3():
    askyesno('Fare Confirm','total amount to be paid')
    root.destroy()
    import ticket.py
def fun1():
       Label(root,text="Fill Passengers Details",font='Cambria 20 bold',fg='Red',bg='LightBlue1').grid(row=6,column=0,columnspan=10,pady=1000//10)
       Label(root,text="Name",font='Cambria 10').grid(row=7,column=0,pady=1000//50)
       Entry(root).grid(row=7,column=1)
       Label(root,text="Gender",font='Cambria 10').grid(row=7,column=2)
       gender=StringVar()
       opt=["male","Female","Others"]
       gender.set("")
       d_menu=OptionMenu(root,gender,*opt).grid(row=7,column=3)
       Label(root,text="NO. Of Seats",font='Cambria 10').grid(row=7,column=4)
       Entry(root).grid(row=7,column=5)
       Label(root,text="Mobile.NO",font='Cambria 10').grid(row=7,column=6)
       Entry(root).grid(row=7,column=7)
       Label(root,text="Age",font='Cambria 10').grid(row=7,column=8)
       Entry(root).grid(row=7,column=9)
       Button(root,text="Book Seat",font='Cambria 10',bg='green',command=fun3).grid(row=7,column=10)
def fun():
    Label(root,text="Select Bus",font='Cambria 10 bold',fg='green').grid(row=4,column=0,pady=200//16)
    Label(root,text="Operator",font='Cambria 10',fg='green').grid(row=4,column=1)
    Label(root,text="Bus Type",font='Cambria 10',fg='green').grid(row=4,column=2)
    Label(root,text="Available Capacity",font='Cambria 10',fg='green').grid(row=4,column=3)
    Label(root,text="Fare",font='Cambria 10',fg='green').grid(row=4,column=4)
    Radiobutton(root,text="Bus1",bg='palegreen4').grid(row=5,column=0)
    Button(root,text="Proceed To Book",font='Cambria 10',bg='green',command=fun1).grid(row=5,column=8)
def close():
    root.destroy()
    import options.py
Button(root,text="show bus",bg='Green3',command=fun).grid(row=3,column=8)
home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=close).grid(row=3,column=9)
import sqlite3
con=sqlite3.connect("bus.db")
cur=con.cursor()
root.mainloop()
