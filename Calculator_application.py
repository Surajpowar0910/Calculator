from tkinter import *
import tkinter
from tkinter import messagebox

def clear():
    E4.delete(0,END)
    E3.delete(0,END)
    E2.delete(0,END)
    E1.delete(0,END)
    return

# Basic operation of calculator.
def operation():
    try:
        number1=Entry.get(E1)
        number2=Entry.get(E2)
        operator=Entry.get(E3)
        number1=float(number1)
        number2=float(number2)
        if operator =="+":
            answer=number1+number2
        if operator =="-":
            answer=number1-number2
        if operator =="*":
            answer=number1*number2
        if operator =="/":
            answer=number1/number2
        if operator =="%":
            answer= (number2/number1)*100
        Entry.insert(E4,0,answer)
        
        
        print(answer)
    except ValueError:
        messagebox.showwarning("Warning","Kindly enter the numeric value.")


# Interface of Calculator using Tkinter.
top  =Tk()
top.config(background = "powder blue")
top.geometry("250x240")

L1 = Label(top, text="Calculator",).grid(row=0,column=1)
L2 = Label(top, text="Number 1",).grid(row=1,column=0)
L3 = Label(top, text="Number 2",).grid(row=2,column=0)
L4 = Label(top, text="Operator",).grid(row=3,column=0)
L4 = Label(top, text="Answer",).grid(row=4,column=0)
E1 = Entry(top,bd = 5)
E1.grid(row=1,column=1)
E2 = Entry(top,bd = 5)
E2.grid(row=2,column=1)
E3 = Entry(top,bd = 5)
E3.grid(row=3,column=1)
E4 = Entry(top,bd = 5)
E4.grid(row=4,column=1)
B=Button(top,text ="Submit", command=operation , relief=RAISED).grid(row=5,column=1)
B_1=Button(top,text="Clear", command= clear , relief= RAISED).grid(row=6,column=1)
B1=Button(top,text ="Quit", relief=RAISED, command= top.destroy).grid(row=7,column=1)

top.mainloop()
