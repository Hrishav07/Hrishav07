from tkinter import*
from tkinter.messagebox import*
root=Tk()
root.geometry('10000000x10000000')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,columnspan=10,padx=(1000//3))
Label(root,text="Online Bus Booking System",font='Cambria 20 bold',fg='red',bg='cyan2').grid(row=1,column=1,columnspan=10)
Label(root,text="Add Bus Runnig Details",font='Cambria 18 bold',fg='Dark green').grid(row=2,column=1,columnspan=10,pady=1000//55)
Label(root,text="Busid",font='Cambria 10').grid(row=3,column=0)
Entry(root).grid(row=3,column=1)
Label(root,text="Running date",font='Cambria 10').grid(row=3,column=2)
Entry(root).grid(row=3,column=3)
Label(root,text="seat available",font='Cambria 10').grid(row=3,column=4)
Entry(root).grid(row=3,column=5)
def ra():
    showinfo('information','run added succesfully')
def rd():
     showinfo('information','run deleted succesfully')
Button(root,text="Add Run",bg='lime green',command=ra).grid(row=3,column=6)
Button(root,text="Delete Route",fg='red',bg='lime green',command=rd).grid(row=3,column=7)
def close():
    root.destroy()
    import options.py
home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=close).grid(row=4,column=4)
root.mainloop()
