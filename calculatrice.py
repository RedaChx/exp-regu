import tkinter

win = tkinter.Tk()
win.title("Calculatrice")
win.geometry("500x500")
win.config(bg="purple")

L1 = tkinter.Label(text="Nombre 1 ", bg="purple")
L1.place(x=30,y=40)
Z1 = tkinter.Entry()
Z1.place(x=110,y=40)
Z4 = tkinter.Entry()
Z4.place(x=180,y=70,width=50)
L2 = tkinter.Label(text="Nombre 2 ", bg="purple")
L2.place(x=30,y=100)
Z2 = tkinter.Entry()
Z2.place(x=110,y=100)
L3 = tkinter.Label(text="Resultat :", bg="purple")
L3.place(x=30,y=140)
Z3 = tkinter.Entry()
Z3.place(x=110,y=140)
def ok():
    but2.config(state="normal")
    Z4.delete(0, tkinter.END)
    if var.get() == "+":
        Z4.insert(0,"+")
    elif var.get() == "-":
        Z4.insert(0,"-")
    elif var.get() == "*":
        Z4.insert(0,"*")
    elif var.get() == "/":
        Z4.insert(0,"/")

L4 = tkinter.Label(text="Operations",bg="purple",fg="cyan")
L4.place(x=330,y=15)
var = tkinter.StringVar()
radio1 = tkinter.Radiobutton(text="Addition",variable=var,value="+",bg="purple",command=ok)
radio1.place(x=330,y=40)
radio1 = tkinter.Radiobutton(text="Soustraction",variable=var,value="-",bg="purple",command=ok)
radio1.place(x=330,y=70)
radio1 = tkinter.Radiobutton(text="Multiplication",variable=var,value="*",bg="purple",command=ok)
radio1.place(x=330,y=100)
radio1 = tkinter.Radiobutton(text="Division",variable=var,value="/",bg="purple",command=ok)
radio1.place(x=330,y=130)

def clear():
    var.set(0)
    Z1.delete(0,tkinter.END)
    Z2.delete(0,tkinter.END)
    Z3.delete(0,tkinter.END)
but1 = tkinter.Button(text="Remise a blanc ",command=clear)
but1.place(x=40,y=190)
def run():
    a = Z1.get()
    b = Z2.get()
    if a.isdigit() or b.isdigit():
        a = int(a)
        b = int(b)
        Z3.delete(0,tkinter.END)
    if var.get() == "+" :
        Z3.insert(0,a + b)
    elif var.get() == "-" :
        Z3.insert(0,a - b)
    elif var.get() == "*" :
        Z3.insert(0,a * b)
    elif var.get() == "/" :
        if b != 0:
            Z3.insert(0,a / b)
    else:
        but2.config(state="normal")
but2 = tkinter.Button(text="OK ",command=run)
but2.place(x=190,y=190)
but2.config(state="disabled")
win.mainloop()
