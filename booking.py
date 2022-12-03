from tkinter import *
from tkinter.messagebox import*
root=Tk()
root.geometry('10000x10000')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=(1000//3))
Label(root,text="Online Bus Booking System",font='Cambria 20 bold',fg='Red',bg='LightBlue1').grid(row=1,column=0,columnspan=10)
Label(root,text="Check Your Booking",font='cambria 15 bold',fg='green4',bg='green2').grid(row=2,column=0,columnspan=10,pady=100/25)
Label(root,text="Enter Your Mobile NO:",font='Calabria 10').grid(row=3,column=3,columnspan=2,pady=1000//50)
Entry(root).grid(row=3,column=5)
def fun():
    fr=LabelFrame(root)
    fr=LabelFrame(root)
    fr.grid(row=4,column=0,columnspan=10)
    Label(fr,text="Passangers:Hrishav Sharma",font='Cambria 15').grid(row=5,column=0)
    Label(fr,text="Gender:Male",font='Cambria 15').grid(row=5,column=1)
    Label(fr,text="NO.Of Seats:",font='Cambria 15').grid(row=6,column=0)
    Label(fr,text="Phone:7898411499",font='Cambria 15').grid(row=6,column=1)
    Label(fr,text="Age:21",font='Cambria 15').grid(row=7,column=0)
    Label(fr,text="Fare.RS:",font='Cambria 15').grid(row=7,column=1)
    Label(fr,text="Booking REF",font='Cambria 15').grid(row=8,column=0)
    Label(fr,text="Bus Detail:",font='Cambria 15').grid(row=8,column=1)
    Label(fr,text="Travel on:",font='Cambria 15').grid(row=9,column=0)
    Label(fr,text="Booked on:",font='Cambria 15').grid(row=9,column=1)
    Label(fr,text="No.Of Seats",font='Cambria 15').grid(row=10,column=0)
    Label(fr,text="Boarding pt:",font='Cambria 15').grid(row=10,column=1)
    Label(fr,text="*Total Amount to be paid at time of boarding the bus",font='Cambria 8').grid(row=11,column=0)
Button(root,text="check booking",font='Calabria 10',command=fun).grid(row=3,column=6)
answer=askyesno('no booking record','do you want to book seat now')
if answer=='no':
    root.destroy()
    import options.py
def closer():
    askyesno('not found','do you want to book ticket')
    if answer=='yes':
        def close():
            root.destroy()
            import journey_details.py
    else:
        def close1():
            root.destroy()
        root.after(1000,close)
def end():
    showinfo('greeting','thanks for taking our services')
    root.destroy()
    import options.py
root.after(14000,end)
root.mainloop()
