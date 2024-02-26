import tkinter
import re

win1 = tkinter.Tk()
win1.geometry("500x500")
win1.title("Checkbox")
win1.config(bg="gray")

def fct2():
    res =""
    if var1.get() == 1:
        res += "Python "
    if var2.get() == 1:
        res += "Java "
    if var3.get() == 1:
        res += "PHP "
    print("vous avez selectionne :"+" "+res+" ")

var1=tkinter.IntVar()
check1=tkinter.Checkbutton(win1 , text="Python ", variable=var1 , bg="gray" )   #on peut utiliser la fonction soit checkbutton ou button
check1.place(x=75,y=10)
var2=tkinter.IntVar()
check2=tkinter.Checkbutton(win1 , text="Java ", variable=var2 , bg="gray" )
check2.place(x=75,y=60)
var3=tkinter.IntVar()
check3=tkinter.Checkbutton(win1 , text="PHP ", variable=var3 , bg="gray" )
check3.place(x=75,y=110)

but1 = tkinter.Button(text="Valider" , command=fct2 , bg="gray" , relief="flat")
but1.place(x=75,y=160)

win1.mainloop()
