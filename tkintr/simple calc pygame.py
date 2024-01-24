from tkinter import *
Calculator=Tk()
Calculator.geometry("700x700")
Calculator.minsize(400,400)
Calculator.title("Calculator")
Number1=Label(Calculator,text="Number 1",font=("Corbel",20))
Number1.place(x=0,y=100)
Number2=Label(Calculator,text="Number 2",font=("Corbel",20))
Number2.place(x=0,y=150)
Operator=Label(Calculator,text="Operator",font=("Corbel",20))
Operator.place(x=0,y=200)
v=IntVar()
y=IntVar()
z=StringVar()
def calculate():
    x=float(v.get())
    u=float(y.get())
    k=z.get()
    if k=="+":
        f=x+u
        Answer.config(text=f)
    elif k=="-":
        f=x-u
        Answer.config(text=f)
    elif k=="/":
        f=x/u
        Answer.config(text=f)
    elif k=="*":
        f=x*u
        Answer.config(text=f)
e1=Entry(Calculator,bd=5,font=("Corbel",20),textvariable=v)
e1.place(x=125, y=100)
e2=Entry(Calculator,bd=5,font=("Corbel",20),textvariable=y)
e2.place(x=125,y=150)
e3=Entry(Calculator,bd=5,font=("Corbel",20),textvariable=z)
e3.place(x=125,y=200)
b1=Button(Calculator,text="Calculate",width=20,height=8,command=calculate)
b1.place(x=425,y=105)
Answer=Label(Calculator,text="RESULT",font=("Corbel",20))
Answer.place(x=0,y=250)
Calculator.mainloop()