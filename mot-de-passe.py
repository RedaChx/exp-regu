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
    if re.search(name, Z1.get()) and re.search(number, Z2.get()) and re.search(email, Z3.get()):
        L4 = tkinter.Label(text="Valide info", bg="purple", fg="green")
        L4.place(x=180, y=220)
    else:
        L5 = tkinter.Label(text="Invalide info", bg="purple", fg="red")
        L5.place(x=180, y=220)
    if re.search(name, Z1.get()):
        l1 = tkinter.Label(text="Valide name", bg="purple", fg="green")
        l1.place(x=380,y=30)
    else:
        l2 = tkinter.Label(text="Invalide name", bg="purple", fg="red")
        l2.place(x=380,y=30)
    if re.search(number, Z2.get()):
        l3 = tkinter.Label(text="Valide Number", bg="purple", fg="green")
        l3.place(x=380,y=75)
    else:
        l4 = tkinter.Label(text="Invalide Number", bg="purple", fg="red")
        l4.place(x=380,y=75)
    if re.search(email, Z3.get()):
        l5 = tkinter.Label(text="Valide Email", bg="purple", fg="green")
        l5.place(x=380,y=120)
    else:
        l6 = tkinter.Label(text="Invalide Email", bg="purple", fg="red")
        l6.place(x=380,y=120)

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
but1 = tkinter.Button(text="Effacer",command=clear)
but1.place(x=180,y=160)
but2 = tkinter.Button(text="Valider",command=validate)
but2.place(x=280,y=160)


window.mainloop()
