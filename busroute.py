from tkinter import*
from tkinter.messagebox import*
root=Tk()
root.geometry('10000000x10000000')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=(1000//3))
Label(root,text="Online Bus Booking System",font='Cambria 20 bold',fg='red',bg='cyan2').grid(row=1,column=0,columnspan=10)
Label(root,text="Add Bus Route Details",font='Cambria 18 bold',fg='Dark green').grid(row=2,column=0,columnspan=10,pady=1000//55)
Label(root,text="Routeid",font='Cambria 10').grid(row=3,column=0)
Entry(root).grid(row=3,column=1)
Label(root,text="station Name",font='Cambria 10').grid(row=3,column=2)
Entry(root).grid(row=3,column=3)
Label(root,text="Station id",font='Cambria 10').grid(row=3,column=4)
Entry(root).grid(row=3,column=5)
def add():
    showinfo('details','new route added')
def delete():
    showinfo('delete','route deleted succesfully')
Button(root,text="Add Route",bg='lime green',command=add).grid(row=3,column=6)
Button(root,text="Delete Route",fg='red',bg='lime green',command=delete).grid(row=3,column=7)
def close():
    root.destroy()
    import details_option.py
home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=close).grid(row=4,column=4)
root.mainloop()
