from tkinter import*
from tkinter.messagebox import*
root=Tk()
root.geometry('1000x1000')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=(1000//3))
Label(root,text="Online Bus Booking System",font='Cambria 20 bold',fg='red',bg='sky blue').grid(row=1,column=0)
Label(root,text="Name: HRISHAV SHARMA",font='Cambria 10',fg='navy').grid(row=3,column=0,pady=(1000//50))
Label(root,text="Enr : 211B138",font='Cambria 10',fg='navy').grid(row=5,column=0,pady=(1000//50))
Label(root,text="Mobile: 7898411499",font='Cambria 10',fg='navy').grid(row=7,column=0,pady=(1000//50))
Label(root,text="Submitted to: DR. Mahesh Kumar",font='Cambria 20 bold',fg='red',bg='sky blue').grid(row=9,column=0)
Label(root,text="Project Based Learnig",font='Cambria 15 bold',fg='red').grid(row=10,column=0)
def close():
    root.destroy()
    import options.py
root.after(6000,close)

root.mainloop()
