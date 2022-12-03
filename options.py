from tkinter import *
from tkinter.messagebox import*
root=Tk()
root.geometry('1000x1000')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=(1000//3))
Label(root,text="Online Bus Booking System",font='Cambria 20 bold',fg='Red',bg='sky blue').grid(row=1,column=0,columnspan=3)
def close():
    root.destroy()
    import journey_details.py
def close1():
    root.destroy()
    import booking.py
def close2():
    root.destroy()
    import details_option.py
Button(root,text="Seat Booking",font='Cambria 20 bold',fg='black',bg='lime green',command=close).grid(row=2,column=0,pady=(1000//50))
Button(root,text="Check Booked details",font='Cambria 20 bold',fg='black',bg='forest green',command=close1).grid(row=2,column=1,pady=(1000//50))
Button(root,text="Add Bus Details",font='Cambria 20 bold',fg='black',bg='dark green',command=close2).grid(row=2,column=2,pady=(1000//50))
Label(root,text="For Admin Only",font='Arial 10',fg='red').grid(row=3,column=2,pady=(1000//100))
root.mainloop()
