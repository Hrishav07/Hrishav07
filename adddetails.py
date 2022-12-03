from tkinter import *
from tkinter.messagebox import*
root=Tk()
root.geometry('10000x10000')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=(10000//30))
Label(root,text="Online Bus Booking System",font='Cambria 20 bold',fg='Red',bg='LightBlue1').grid(row=1,column=0,columnspan=10)
Label(root,text="Add Bus OPERATOR Details",font='Cambria 18 bold',fg='green4').grid(row=2,column=1,columnspan=10)
Label(root,text="Operator id",font='Cambria 10').grid(row=3,column=0,pady=(10000//300))
Entry(root).grid(row=3,column=1)
Label(root,text="name",font='Cambria 10').grid(row=3,column=2)
Entry(root).grid(row=3,column=3)
Label(root,text="Address",font='Cambria 10').grid(row=3,column=4)
Entry(root).grid(row=3,column=5)
Label(root,text="phone",font='Cambria 10').grid(row=3,column=6)
Entry(root).grid(row=3,column=7)
Label(root,text="Email",font='Cambria 10').grid(row=3,column=8)
Entry(root).grid(row=3,column=9)
def fun():
    showinfo('operator entry','opoerator record added')
Button(root,text="Add",bg='green',command=fun).grid(row=3,column=10)
def fun1():
    showinfo('operator entry update','operator record update succesfully') 
Button(root,text="Edit",bg='green',command=fun1).grid (row=3,column=11)
def close():
    root.destroy()
    import options.py
home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=close).grid(row=4,column=8)
root.mainloop()
