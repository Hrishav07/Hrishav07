from tkinter import*
from tkinter.messagebox import*
root=Tk()
root.geometry('1000000x1000000')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=(1000//3))
Label(root,text="Online Bus Booking System",font='Cambria 20 bold',fg='red',bg='cyan2').grid(row=1,column=0,columnspan=10)
Label(root,text="ADD NEW DETAILS TO DATABASE",font='Cambria 12 bold',fg='green').grid(row=2,column=0,pady=1000//50,columnspan=10)
def close():
    root.destroy()
    import adddetails.py
def close1():
    root.destroy()
    import newbus.py
def close2():
    root.destroy()
    import busroute.py
def close3():
    root.destroy()
    import busrun.py
Button(root,text="New Operator",font='Cambria 10',bg='green',command=close).grid(row=3,column=0)
Button(root,text="New Bus",font='Cambria 10',bg='orangered2',command=close1).grid(row=3,column=1,columnspan=10)
Button(root,text="New Route",font='Cambria 10',bg='Royalblue1',command=close2).grid(row=3,column=2)
Button(root,text="New Run",font='Cambria 10',bg='sienna3',command=close3).grid(row=3,column=5,columnspan=10)
def home():
    root.destroy()
    import options.py
Button(root,text="HOME",font='Cambria 10',bg='red',command=home).grid(row=3,column=8)
root.mainloop()
