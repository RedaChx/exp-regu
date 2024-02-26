import tkinter
import re

window=tkinter.Tk()
window.title("mot de passe")
window.geometry("500x500")
window.config(bg="purple")

L1 = tkinter.Label(text="Saisir votre Nom :",bg="purple")
L1.place(x=20,y=30)
Z1 = tkinter.Entry()
Z1.place(x=180,y=30)
L2 = tkinter.Label(text="Saisir votre Telephone :",bg="purple")
L2.place(x=20,y=75)
Z2 = tkinter.Entry()
Z2.place(x=180,y=75)
L3 = tkinter.Label(text="Saisir votre Email :",bg="purple")
L3.place(x=20,y=120)
Z3 = tkinter.Entry()
Z3.place(x=180,y=120)

def clear():
    Z1.delete(0,tkinter.END)
    Z2.delete(0,tkinter.END)
    Z3.delete(0,tkinter.END)
def validate():
    name = "^[A-Z][a-z]{2,9}$"
    number = "^(06|07)[0-9]{8}$"
    email = "^[a-zA-Z]+[a-zA-Z0-9_.-]*@[A-Za-z0-9_.-]+\.[a-zA-Z]{2,}$"
    a = Z1.get()
    b = Z2.get()
    c = Z3.get()
    if re.search(name, a) and re.search(number, b) and re.search(email, c):
        L4 = tkinter.Label(text="Valid info", bg="purple", fg="green")
        L4.place(x=180, y=220)
        """
        window.destroy()
        """
        new = tkinter.Tk()
        new.geometry("300x300")
        new.title("Infos")
        new.config(bg="gray")

        label1 = tkinter.Label(new , text="Bonjour"+" "+a , bg="gray")
        label1.pack()
        label2 = tkinter.Label(new , text="Votre Email est :"+" "+c , bg="gray")
        label2.place(x=10,y=50)
        label3 = tkinter.Label(new , text="Votre Telephone est :"+" "+b , bg="gray")
        label3.place(x=10,y=80)

        new.mainloop()
    else:
        L5 = tkinter.Label(text="Invalid info", bg="purple", fg="red")
        L5.place(x=180, y=220)
    if re.search(name, a):
        l1 = tkinter.Label(text="Valid name", bg="purple", fg="green")
        l1.place(x=380,y=30)
    else:
        l2 = tkinter.Label(text="Invalid name", bg="purple", fg="red")
        l2.place(x=380,y=30)
    if re.search(number, b):
        l3 = tkinter.Label(text="Valid Number", bg="purple", fg="green")
        l3.place(x=380,y=75)
    else:
        l4 = tkinter.Label(text="Invalid Number", bg="purple", fg="red")
        l4.place(x=380,y=75)
    if re.search(email, c):
        l5 = tkinter.Label(text="Valid Email", bg="purple", fg="green")
        l5.place(x=380,y=120)
    else:
        l6 = tkinter.Label(text="Invalid Email", bg="purple", fg="red")
        l6.place(x=380,y=120)

but1 = tkinter.Button(text="Effacer",command=clear)
but1.place(x=230,y=160)
but2 = tkinter.Button(text="Valider",command=validate)
but2.place(x=320,y=160)

window.mainloop()
"""
def validate():
    nom="^[A-Z]{1}[a-z]{2,9}$"
    tel="^(06|07)[0-9]{8}$"
    email="^[a-zA-z]+[a-zA-z0-9_.-]+@[A-Za-z0-9_.-]+[a-z]+\.[a-z]{3}$"
    if re.search(Z1.get(),nom) and re.search(Z2.get(),tel) and re.search(Z3.get(),email) :
        L4 = tkinter.Label(text="Valide info",bg="purple",fg="green")
        L4.place(x=180,y=220)
    else:
        L5 = tkinter.Label(text="Invalide info",bg="purple",fg="red")
        L5.place(x=180,y=220)
"""

