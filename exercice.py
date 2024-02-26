import tkinter

win = tkinter.Tk()
win.geometry("500x100")
win.title("Ma Fenetre")
win.config(bg="purple")

def Afficher():
    if var1.get() == 1 :
        win.geometry("500x200")
        L1 = tkinter.Label(win , text="Couleurs" , bg="purple")
        L1.place(x=30,y=80)
        def color():
            if var.get() == 1 :
                win.config(bg="red")
                L1.config(bg="red")
                radio1.config(bg="red")
                radio2.config(bg="red")
                radio3.config(bg="red")
                check1.config(bg="red")
            if var.get() == 2 :
                win.config(bg="green")
                L1.config(bg="green")
                radio1.config(bg="green")
                radio2.config(bg="green")
                radio3.config(bg="green")
                check1.config(bg="green")
            if var.get() == 3 :
                win.config(bg="blue")
                L1.config(bg="blue")
                radio1.config(bg="blue")
                radio2.config(bg="blue")
                radio3.config(bg="blue")
                check1.config(bg="blue")
        var = tkinter.IntVar()
        radio1 = tkinter.Radiobutton(win , text="Rouge" ,variable=var , value=1 , bg="purple", command=color)
        radio1.place(x=30,y=120)
        radio2 = tkinter.Radiobutton(win , text="Vert" ,variable=var , value=2 , bg="purple", command=color)
        radio2.place(x=120,y=120)
        radio3 = tkinter.Radiobutton(win , text="Bleu" ,variable=var , value=3 , bg="purple", command=color)
        radio3.place(x=200,y=120)
    
var1 = tkinter.IntVar()
check1 = tkinter.Checkbutton(win , text="Afficher les couleur" , variable=var1 , bg="purple" , command=Afficher)
check1.place(x=30,y=30)

def reset():
    check1.deselect()
    win.geometry("500x100")
    win.config(bg="purple")
    check1.config(bg="purple")

but1 = tkinter.Button(win , text="Quitter" , command=reset)
but1.place(x=230,y=30)

win.mainloop()
